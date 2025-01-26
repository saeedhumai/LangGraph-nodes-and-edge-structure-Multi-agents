from typing import Annotated
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

# Initialize REPL
repl = PythonREPL()

@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute."],
):
    """Use this to execute python code and do math."""
    try:
        result = repl.run(code)
        return f"Successfully executed:\n```python\n{code}\n```\nOutput: {result}"
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}" 