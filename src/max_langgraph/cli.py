"""Command-line entry point for the starter graph."""

import argparse

from .graph import run_agent


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description="Run the Max LangGraph starter workflow.")
    parser.add_argument("topic", help="Topic to pass through the graph")
    return parser.parse_args()


def main() -> None:
    """Run the graph and print the final answer."""

    args = parse_args()
    result = run_agent(args.topic)
    print(result["final"])


if __name__ == "__main__":
    main()
