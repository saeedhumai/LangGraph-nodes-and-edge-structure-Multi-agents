import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.agents.graph import create_graph

def format_agent_response(step):
    """Format the agent response in a clean way."""
    # Unpack the step
    agent_info, state = step
    
    # Handle agent name
    if isinstance(agent_info, tuple) and len(agent_info) > 0:
        agent_name = agent_info[0].split(':')[0]
    else:
        # Get the first key from state that has messages
        for key in state:
            if 'messages' in state[key]:
                agent_name = key
                break
        else:
            return None
    
    # Get messages if they exist
    if agent_name not in state or 'messages' not in state[agent_name]:
        return None
    
    # Get the message
    message = state[agent_name]['messages'][0]
    if not message.content:
        return None
    
    # Format the response
    display_name = message.name if hasattr(message, 'name') else agent_name
    return f"{display_name.capitalize()}: {message.content}"

def main():
    # Load environment variables
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini", 
        openai_api_key=openai_api_key,
        temperature=0.7
    )

    # Create the graph
    graph = create_graph(llm)

    # Example usage
    print("\n🤖 Starting conversation...\n")
    print("Question: What's the square root of 42?\n")
    
    for step in graph.stream(
        {"messages": [("user", "What's the square root of 42?")]}, 
        subgraphs=True
    ):
        response = format_agent_response(step)
        if response:
            print(response)
    
    print("\n✨ Conversation completed!\n")

if __name__ == "__main__":
    main() 