from typing import TypedDict, List


class InvestigationState(TypedDict):
    findings: List[str]
    suspicion_score: int
    next_plugin: str
    reasoning: List[str]
    plugin_output: str
    report: str
