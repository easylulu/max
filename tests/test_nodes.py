from max_langgraph.nodes import collect_context, draft_answer, review_answer
from max_langgraph.state import AgentState


def initial_state(topic: str = "LangGraph 项目") -> AgentState:
    return {"topic": topic, "research_notes": [], "draft": "", "final": ""}


def test_collect_context_uses_topic() -> None:
    result = collect_context(initial_state("客服助手"))

    assert result["research_notes"][0] == "Define the goal for 客服助手."
    assert len(result["research_notes"]) == 3


def test_draft_and_review_create_final_answer() -> None:
    state = initial_state()
    state.update(collect_context(state))
    state.update(draft_answer(state))
    state.update(review_answer(state))

    assert "Plan for LangGraph 项目" in state["draft"]
    assert "Next step:" in state["final"]
