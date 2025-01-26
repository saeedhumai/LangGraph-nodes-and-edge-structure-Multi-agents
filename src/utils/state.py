from typing_extensions import TypedDict
from langgraph.graph import MessagesState
from src.config.settings import OptionLiteral

class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""
    next: OptionLiteral

class State(MessagesState):
    """State class that extends MessagesState to include next worker."""
    next: str 