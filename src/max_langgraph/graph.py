"""LangGraph workflow assembly."""

from langgraph.graph import END, START, StateGraph

from .nodes import collect_context, draft_answer, review_answer
from .state import AgentState


def build_graph():
    """Compile and return the starter LangGraph application."""

    workflow = StateGraph(AgentState)
    workflow.add_node("collect_context", collect_context)
    workflow.add_node("draft_answer", draft_answer)
    workflow.add_node("review_answer", review_answer)

    workflow.add_edge(START, "collect_context")
    workflow.add_edge("collect_context", "draft_answer")
    workflow.add_edge("draft_answer", "review_answer")
    workflow.add_edge("review_answer", END)

    return workflow.compile()


def run_agent(topic: str) -> AgentState:
    """Run the compiled graph for a topic and return the final state."""

    app = build_graph()
    initial_state: AgentState = {
        "topic": topic,
        "research_notes": [],
        "draft": "",
        "final": "",
    }
    return app.invoke(initial_state)
