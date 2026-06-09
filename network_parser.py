def parse_netscan(output):

    connections = []

    lines = output.splitlines()

    for line in lines:

        parts = line.split()

        if len(parts) < 9:
            continue

        if not parts[0].startswith("0x"):
            continue

        connection = {
            "proto": parts[1],
            "local_addr": parts[2],
            "local_port": parts[3],
            "foreign_addr": parts[4],
            "foreign_port": parts[5],
            "pid": parts[7],
            "owner": parts[8]
        }

        connections.append(connection)

    return connections


def analyze_network(connections):

    findings = []

    for conn in connections:

        if conn["owner"].lower() == "tcpsvcs.exe":
            findings.append(
                "TCPSVCS.EXE listening on network ports"
            )

        if conn["foreign_addr"] not in ["*", "0.0.0.0", "::"]:
            findings.append(
                f"External connection observed: {conn['foreign_addr']}"
            )

    return list(set(findings))
