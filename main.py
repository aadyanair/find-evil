from agent.graph import graph

result = graph.invoke(
    {
        "findings": [],
        "network_findings": [],
        "suspicion_score": 0,
        "next_plugin": "",
        "reasoning": [],
        "plugin_output": "",
        "report": ""
    }
)

# Save report to file
with open("investigation_report.txt", "w") as f:
    f.write(result["report"])

# Print report to terminal
print(result["report"])

print("\nReport saved to investigation_report.txt")
