from langgraph.graph import StateGraph, END

from agent.state import InvestigationState
from agent.nodes import (
    analyze_node,
    network_node,
    score_node,
    decision_node,
    reasoning_node,
    execute_plugin_node,
    report_node
)

builder = StateGraph(InvestigationState)

builder.add_node("analyze", analyze_node)
builder.add_node("network", network_node)
builder.add_node("score", score_node)
builder.add_node("decision", decision_node)
builder.add_node("reasoning", reasoning_node)
builder.add_node("execute_plugin", execute_plugin_node)
builder.add_node("report", report_node)

builder.set_entry_point("analyze")

builder.add_edge("analyze", "network")
builder.add_edge("network", "score")
builder.add_edge("score", "decision")
builder.add_edge("decision", "reasoning")
builder.add_edge("reasoning", "execute_plugin")
builder.add_edge("execute_plugin", "report")
builder.add_edge("report", END)

graph = builder.compile()
