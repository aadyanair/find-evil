from network_parser import parse_netscan, analyze_network

with open("netscan_output.txt", "r") as f:
    output = f.read()

connections = parse_netscan(output)

findings = analyze_network(connections)

print(findings)
