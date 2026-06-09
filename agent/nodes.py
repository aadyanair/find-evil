from parser import parse_processes
from volatility_runner import run_plugin
from network_parser import parse_netscan, analyze_network


def analyze_node(state):

    with open("pslist_output.txt", "r") as f:
        output = f.read()

    findings = parse_processes(output)

    return {
        "findings": findings
    }


def score_node(state):

    findings = state["findings"]

    suspicious = {
        "powershell.exe": 30,
        "cmd.exe": 20,
        "wscript.exe": 40,
        "cscript.exe": 40,
        "rundll32.exe": 25,
        "winrar.exe": 10,
        "dumpit.exe": 15
    }

    score = 0

    for process in findings:

        process = process.lower()

        if process in suspicious:
            score += suspicious[process]

    return {
        "suspicion_score": score
    }


def decision_node(state):

    score = state["suspicion_score"]

    if score >= 40:
        plugin = "windows.cmdline"

    elif score >= 20:
        plugin = "windows.netscan"

    else:
        plugin = None

    return {
        "next_plugin": plugin
    }


def reasoning_node(state):

    findings = state["findings"]

    reasoning = []

    for process in findings:

        p = process.lower()

        if p == "cmd.exe":
            reasoning.append(
                "Command shell activity detected"
            )

        elif p == "winrar.exe":
            reasoning.append(
                "Archive utility detected"
            )

        elif p == "dumpit.exe":
            reasoning.append(
                "Memory acquisition software detected"
            )

    return {
        "reasoning": reasoning
    }


def execute_plugin_node(state):

    plugin = state["next_plugin"]

    if not plugin:
        return {
            "plugin_output": "No plugin executed"
        }

    output, error = run_plugin(
        "evidence/MemoryDump_Lab1.raw",
        plugin
    )

    return {
        "plugin_output": output[:1000]
    }


def report_node(state):

    report = f"""
=============================
      INVESTIGATION REPORT
=============================

Process Findings:
{state['findings']}

Network Findings:
{state['network_findings']}

Suspicion Score:
{state['suspicion_score']}

Recommended Plugin:
{state['next_plugin']}

Reasoning:
{state['reasoning']}

Plugin Output Preview:
{state['plugin_output']}
"""

    return {
        "report": report
    }    
def network_node(state):

    with open("netscan_output.txt", "r") as f:
        output = f.read()

    connections = parse_netscan(output)

    findings = analyze_network(connections)

    return {
        "network_findings": findings
    }
