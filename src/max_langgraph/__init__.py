"""LangGraph starter package for Max."""

__all__ = ["build_graph", "run_agent"]


def __getattr__(name: str):
    """Lazily expose graph helpers without importing LangGraph during pure-node tests."""

    if name in __all__:
        from .graph import build_graph, run_agent

        return {"build_graph": build_graph, "run_agent": run_agent}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
