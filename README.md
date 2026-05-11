# Max LangGraph Starter

这是一个基于 **LangGraph 最新稳定版 1.1.10** 的 Python 起始项目。PyPI 在 2026-04-27 发布了 1.1.10，并标记 Python 要求为 `>=3.10`，因此本项目的依赖范围固定为 `langgraph>=1.1.10,<1.2.0`，避免自动安装 1.2 预发布版。

## 项目结构

```text
.
├── pyproject.toml          # 项目元数据、依赖、CLI 入口、测试配置
├── src/max_langgraph/
│   ├── state.py            # LangGraph 共享状态类型
│   ├── nodes.py            # 可单元测试的纯节点函数
│   ├── graph.py            # StateGraph 组装和编译
│   └── cli.py              # 命令行入口
└── tests/test_nodes.py     # 不依赖外部 LLM 的节点测试
```

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
max-langgraph "构建一个客服助手"
```

也可以直接运行模块：

```bash
python -m max_langgraph.cli "构建一个客服助手"
```

## 工作流说明

当前工作流是一个可离线运行的确定性三节点图：

1. `collect_context`：根据输入主题生成上下文笔记。
2. `draft_answer`：把笔记汇总成草稿。
3. `review_answer`：生成最终输出并给出下一步建议。

入口在 `build_graph()`：

```python
workflow = StateGraph(AgentState)
workflow.add_node("collect_context", collect_context)
workflow.add_node("draft_answer", draft_answer)
workflow.add_node("review_answer", review_answer)
```

## 下一步扩展

- 在 `nodes.py` 中把确定性节点替换为 LLM 调用或工具调用。
- 添加 checkpointer 以支持短期记忆和可恢复执行。
- 接入 LangSmith 以观察每个节点的输入、输出和耗时。
