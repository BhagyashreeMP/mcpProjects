# Leave Management MCP Server

A Python-based **MCP (Multi-Connector Platform) server** designed for managing employee leave information. Built using **FastMCP**, this server exposes **tools**, **resources**, and **prompts** that can be called dynamically through **Claude Desktop** or any compatible MCP client.

---

## Features

### Tools
- **Calculate Remaining Leaves**: Compute how many leaves an employee has left based on total and used leaves.
- **Get Leave Balance by Employee ID**: Fetch the remaining leaves for a specific employee using their ID.
- **Apply Leave**: Submit a leave request for an employee if sufficient balance exists. Provides success/failure messages.

### Resources
- **Employee Leave Status**: Returns detailed leave status for a given employee including total, used, and remaining leaves, plus pending requests.
- **Personalized Greeting**: Returns a greeting message for a given employee or user.

### Prompts
- **Generate Leave Request**: Generates a leave request message in **polite**, **formal**, or **casual** style based on user input.
- **Greet User**: Generates a greeting in a selected style such as friendly, formal, or casual.

---

## Project Structure

```
leave-management-mcp/
│
├── main.py             # MCP server definition with tools, resources, and prompts
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .claude/            # Optional: Claude Desktop MCP configuration
```

---

## Installation Steps

1. **Clone the repository**

```bash
git clone <repository-url>
cd leave-management-mcp
```

2. **Install dependencies**

Ensure Python 3.10+ is installed, then:

```bash
pip install fastmcp
```

---

## Running the Server

1. **Start the MCP server**

Run the server using Python. You should see a confirmation message indicating that the server is running.

2. **Testing the Server**

- Test **tools** directly in Python by importing them from the main server module.
- Access **resources** via MCP-compatible clients or HTTP endpoints if exposed.
- Use **prompts** to generate human-readable text outputs.

---

## Claude Desktop Integration (Local Setup)

Since the Claude MCP configuration is **local to your system**, follow these steps:

1. **Locate your local MCP config file**:

- **Windows:** `%USERPROFILE%\.claude\mcpServers.json`
- **Linux/macOS:** `~/.claude/mcpServers.json`

This file stores all MCP server configurations for Claude Desktop.

2. **Add Leave Management MCP server manually**:

Open the JSON file in a text editor and add an entry for your server, specifying the path to your `main.py`:

```json
{
  "mcpServers": {
    "LeaveManagement": {
      "command": "python",
      "args": [
        "C:\\Users\\<YourUsername>\\Documents\\Projects\\leave-management-mcp\\main.py"
      ]
    }
  }
}
```

> Replace `<YourUsername>` with your actual Windows username or adjust the path for Linux/macOS.

3. **Save the file and restart Claude Desktop.**

After restarting, the Leave Management server should appear in the **connectors list**, ready for prompt-style queries.

4. **Using the MCP Server in Claude**:

- Ask Claude to **greet an employee**, **check leave balance**, or **generate a leave request**.
- Claude will automatically call the corresponding **tool**, **resource**, or **prompt** and display the output.

---

## Notes

- The MCP server is modular: you can **add new tools, prompts, and resources** for other HR or business workflows.
- All tools return Python-native types suitable for JSON serialization.
- Prompts are designed to produce **human-readable messages**, making them ideal for AI assistant responses.

---

## Dependencies

- Python 3.10+
- **FastMCP**: A Python framework for building MCP servers.

Install dependencies using:

```bash
pip install fastmcp
```

---

## License

MIT License — free to use and extend for personal or organizational projects.