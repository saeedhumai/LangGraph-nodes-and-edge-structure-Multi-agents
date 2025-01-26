from typing import Literal
from langgraph.graph import END
from langgraph.types import Command
from src.utils.state import State, Router
from src.config.settings import SYSTEM_PROMPT, TEAM_MEMBERS

def create_supervisor_node(llm):
    """Creates the supervisor node that routes between workers."""
    def supervisor_node(state: State) -> Command[Literal[*TEAM_MEMBERS, "__end__"]]:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
        ] + state["messages"]
        response = llm.with_structured_output(Router).invoke(messages)
        goto = response["next"]
        if goto == "FINISH":
            goto = END

        return Command(goto=goto, update={"next": goto})
    
    return supervisor_node 