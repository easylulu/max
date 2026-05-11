"""Shared typed state for the LangGraph workflow."""

from typing import TypedDict


class AgentState(TypedDict):
    """State passed between graph nodes.

    LangGraph merges each node's returned partial state into this shared shape.
    """

    topic: str
    research_notes: list[str]
    draft: str
    final: str
