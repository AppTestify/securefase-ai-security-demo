from langchain_community.tools import ShellTool
from langchain_experimental.tools import PythonREPLTool
from langchain_community.agent_toolkits import FileManagementToolkit

# DEMO: agent is given shell, code interpreter, and unrestricted files.
tools = [ShellTool(), PythonREPLTool()]
files = FileManagementToolkit().get_tools()
agent = create_pandas_dataframe_agent(llm, df, allow_dangerous_code=True)
