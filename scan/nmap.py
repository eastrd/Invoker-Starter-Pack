import subprocess
import sys
import json
import xml.etree.ElementTree as ET 

def execute_command(cmd):
    try:
        return subprocess.run(cmd, shell=True, check=True, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.STDOUT, 
                                text=True).stdout
    except subprocess.CalledProcessError as e:
        return e.output

def parse_nmap_xml(xml_content):
    root = ET.fromstring(xml_content)
    results = []
    # Find all hosts
    for host in root.findall('./host'):
        address = host.find('address').get('addr')

        address_content = f"## {address}"
        results.append({address_content: []})
        
        # Find all port elements for this host
        for port in host.findall('./ports/port'):
            port_id = port.get('portid')
            protocol = port.get('protocol')
            
            state = port.find('state').get('state')
            
            service = port.find('service')
            if service is not None:
                service_name = service.get('name')
                product = service.get('product', '')
                version = service.get('version', '')
            else:
                service_name = ''
                product = ''
                version = ''
            
            results[-1][address_content].append([f"""### Port: {port_id}/{protocol}""" \
                        + f"\n- Service: {service_name}" if service_name else "" \
                        + f"\n- Product: {product}" if product else "" \
                        + f"\n- Version: {version}" if version else ""])
    return results


scan_result_xml = execute_command(f"nmap -sV -T4 -p- --top-ports 1000 -oX - {sys.argv[1]}")
results = parse_nmap_xml(scan_result_xml)

print(
    json.dumps(
        {
            "type": "Tree",
            "results": results,
        }
    )
)