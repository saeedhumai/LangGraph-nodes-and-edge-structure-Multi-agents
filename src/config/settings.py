from typing import Literal

# Team members configuration
TEAM_MEMBERS = ["researcher", "coder"]
OPTIONS = TEAM_MEMBERS + ["FINISH"]

# System prompt for supervisor
SYSTEM_PROMPT = (
    "You are a supervisor tasked with managing a conversation between the"
    f" following workers: {TEAM_MEMBERS}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)

# Type hints
WorkerLiteral = Literal[*TEAM_MEMBERS]
OptionLiteral = Literal[*OPTIONS] 