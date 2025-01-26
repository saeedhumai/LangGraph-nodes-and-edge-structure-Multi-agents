from langgraph.graph import StateGraph, START
from src.utils.state import State
from src.nodes.supervisor import create_supervisor_node
from src.nodes.workers import create_research_node, create_code_node

def create_graph(llm):
    """Creates the agent graph with all nodes."""
    # Create the nodes
    supervisor_node = create_supervisor_node(llm)
    research_node = create_research_node(llm)
    code_node = create_code_node(llm)

    # Create the graph
    builder = StateGraph(State)
    
    # Add nodes
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("researcher", research_node)
    builder.add_node("coder", code_node)

    # Add edges
    builder.add_edge(START, "supervisor")

    # Compile the graph
    return builder.compile() 




