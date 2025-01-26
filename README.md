# LangGraph Nodes Example

A modular implementation of a multi-agent system using LangGraph. This project demonstrates how to create a supervisor-worker pattern where different agents collaborate to solve tasks.

## Project Structure

```
.
├── src/
│   ├── agents/
│   │   └── graph.py         # Graph creation and configuration
│   ├── config/
│   │   └── settings.py      # Configuration and constants
│   ├── nodes/
│   │   ├── supervisor.py    # Supervisor node implementation
│   │   └── workers.py       # Worker nodes (researcher and coder)
│   └── utils/
│       ├── state.py         # State definitions
│       └── tools.py         # Tool implementations
├── main.py                  # Main execution file
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Features

- **Modular Architecture**: Clean separation of concerns with different components in their own modules
- **Multi-Agent System**: Implements a supervisor-worker pattern
- **Type Safety**: Uses Python type hints throughout the codebase
- **Easy to Extend**: Simple to add new agents or modify existing ones

## Agents

1. **Supervisor**: Routes tasks between workers and decides when work is complete
2. **Researcher**: Provides information and guidance (no calculations)
3. **Coder**: Performs calculations and executes Python code

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the example with:

```bash
python main.py
```

Example output:

```
🤖 Starting conversation...

Question: What's the square root of 42?

Coder: The square root of 42 is approximately 6.48074069840786.

✨ Conversation completed!
```

## Extending the Project

### Adding a New Agent

1. Add the agent name to `src/config/settings.py`
2. Create a new node function in `src/nodes/workers.py`
3. Update the graph in `src/agents/graph.py`

### Adding New Tools

1. Define your tool in `src/utils/tools.py`
2. Update the relevant worker in `src/nodes/workers.py`

## Dependencies

- langchain
- langgraph
- openai
- python-dotenv

## License

MIT

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
