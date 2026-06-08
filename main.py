from agent.graph import graph

result = graph.invoke(
    {
        "findings": [],
        "suspicion_score": 0,
        "next_plugin": "",
        "reasoning": [],
        "plugin_output": "",
        "report": ""
    }
)

print(result["report"])
