import re
import os
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("RegexSearchTool")

@mcp.tool()
def regex_search(file_path: str, pattern: str) -> str:
    """
    Searches for a regex pattern in a file and returns matched lines with their numbers.
    """
    if not os.path.exists(file_path):
        return f"Error: File '{file_path}' not found."

    results = []
    try:
        regex = re.compile(pattern)
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if regex.search(line):
                    results.append(f"Line {line_num}: {line.strip()}")
        
        if not results:
            return "No matches found."
        return "\n".join(results)
    
    except re.error as e:
        return f"Invalid Regex Pattern: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    mcp.run()