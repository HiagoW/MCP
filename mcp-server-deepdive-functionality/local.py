from mcp.server.fastmcp import FastMCP
from pathlib import Path

# Resolve to the folder that *contains* this script
NOTES_FILE = Path(__file__).resolve().with_name("notes.txt")

mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    Args:
        content: The text content to append.
    """

    filename = NOTES_FILE

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Content appended to {filename}."
    except Exception as e:
        return f"Error appending to file {filename}: {e}"
    
@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of the user's local notes.
    """
    filename = NOTES_FILE

    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found."
    except FileNotFoundError:
        return "No notes file found."
    except Exception as e:
        return f"Error reading file {filename}: {e}"
    
if __name__ == "__main__":
    mcp.run()