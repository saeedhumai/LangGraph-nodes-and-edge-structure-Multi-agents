from typing import Literal
from langchain_core.messages import HumanMessage
from langgraph.types import Command
from src.utils.state import State
from src.utils.tools import python_repl_tool
from langgraph.prebuilt import create_react_agent

def create_research_node(llm):
    """Creates the researcher node."""
    research_agent = create_react_agent(
        llm, tools=[], 
        state_modifier="You are a researcher. DO NOT do any math. Just provide information and guidance."
    )

    def research_node(state: State) -> Command[Literal["supervisor"]]:
        result = research_agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="researcher")
                ]
            },
            goto="supervisor",
        )
    
    return research_node

def create_code_node(llm):
    """Creates the coder node."""
    code_agent = create_react_agent(
        llm, 
        tools=[python_repl_tool],
        state_modifier="You are a coder. Use Python to perform calculations and solve problems."
    )

    def code_node(state: State) -> Command[Literal["supervisor"]]:
        result = code_agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="coder")
                ]
            },
            goto="supervisor",
        )
    
    return code_node 