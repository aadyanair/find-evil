def parse_processes(volatility_output):

    processes = []

    lines = volatility_output.splitlines()

    for line in lines:

        parts = line.split()

        if len(parts) < 3:
            continue

        if not parts[0].isdigit():
            continue

        process_name = parts[2]

        processes.append(process_name)

    return list(set(processes))
