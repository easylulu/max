"""Pure node functions used by the LangGraph workflow.

Keeping node logic side-effect free makes it easy to test without requiring an LLM API key.
"""

from .state import AgentState


def collect_context(state: AgentState) -> dict[str, list[str]]:
    """Create deterministic notes for the requested topic."""

    topic = state["topic"].strip()
    return {
        "research_notes": [
            f"Define the goal for {topic}.",
            "List the main constraints, risks, and success criteria.",
            "Prefer small, observable steps so the graph can be extended safely.",
        ]
    }


def draft_answer(state: AgentState) -> dict[str, str]:
    """Build a short draft from collected notes."""

    notes = state.get("research_notes", [])
    bullet_list = "\n".join(f"- {note}" for note in notes)
    return {"draft": f"Plan for {state['topic']}:\n{bullet_list}"}


def review_answer(state: AgentState) -> dict[str, str]:
    """Finalize the draft with a clear next-step recommendation."""

    draft = state.get("draft", "")
    return {
        "final": (
            f"{draft}\n\n"
            "Next step: replace these deterministic nodes with model/tool calls as your "
            "application requirements become clearer."
        )
    }
