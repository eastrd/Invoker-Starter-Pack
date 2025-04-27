import csv
import sys
import json

csv_path = sys.argv[1]
source_col = sys.argv[2]
target_col = sys.argv[3]
relationship_col = sys.argv[4] if len(sys.argv) > 4 else None

nodes_set = set()
sources_set = set()
targets_set = set()
edges = []

with open(csv_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        source = row[source_col].strip()
        target = row[target_col].strip()

        if not source or not target:
            continue  # Skip invalid rows

        nodes_set.add(source)
        nodes_set.add(target)

        sources_set.add(source)
        targets_set.add(target)

        edge = {
            "source": source,
            "target": target,
        }
        if relationship_col and row.get(relationship_col):
            edge["label"] = row[relationship_col].strip()

        edges.append(edge)

# Find origins: nodes that are Source but never Target
origin_nodes = list(sources_set - targets_set)

# Build node objects
nodes = [{"id": node_id, "content": node_id} for node_id in nodes_set]

# Build output
output = {
    "type": "Network",
    "origins": origin_nodes,
    "nodes": nodes,
    "edges": edges,
}

print(json.dumps(output, indent=2, ensure_ascii=False))
