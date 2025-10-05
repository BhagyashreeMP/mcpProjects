from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("LeaveManagement")

# Mock employee leave database
mock_leave_db = {
    "EMP001": {"name": "Anita Sharma", "total_leaves": 20, "used_leaves": 12, "pending_requests": 1},
    "EMP002": {"name": "Ravi Mehta", "total_leaves": 15, "used_leaves": 15, "pending_requests": 0},
    "EMP003": {"name": "Divya Rao", "total_leaves": 25, "used_leaves": 10, "pending_requests": 2},
}

# Tool: Calculate remaining leave balance
@mcp.tool()
def calculate_leave_balance(total_leaves: int, used_leaves: int) -> int:
    """Calculate remaining leave balance"""
    return total_leaves - used_leaves

@mcp.tool()
def get_leave_balance_by_id(employee_id: str) -> str:
    """Fetch remaining leave balance for an employee using ID"""
    data = mock_leave_db.get(employee_id)
    if not data:
        return f"Employee ID '{employee_id}' not found."

    remaining = calculate_leave_balance(data["total_leaves"], data["used_leaves"])
    return f"{data['name']} has {remaining} remaining leave(s)."

# Resource: Get leave details for an employee
@mcp.resource("leave_status://{employee_id}")
def get_leave_status(employee_id: str) -> str:
    """Fetch leave status for the given employee ID"""
    data = mock_leave_db.get(employee_id)
    if not data:
        return "Employee not found."

    remaining = calculate_leave_balance(data["total_leaves"], data["used_leaves"])
    return (
        f"Employee: {data['name']}\n"
        f"Total Leaves: {data['total_leaves']}\n"
        f"Used Leaves: {data['used_leaves']}\n"
        f"Remaining Leaves: {remaining}\n"
        f"Pending Requests: {data['pending_requests']}"
    )

# Prompt: Generate leave application
@mcp.prompt()
def request_leave(name: str, days: int, reason: str, style: str = "polite") -> str:
    """Generate a leave request message"""
    styles = {
        "polite": f"Dear Manager,\n\nI hope this message finds you well. I would like to request {days} day(s) of leave due to {reason}.",
        "formal": f"Respected Sir/Madam,\n\nI am writing to formally request {days} day(s) leave on account of {reason}.",
        "casual": f"Hi, I need {days} day(s) off for {reason}. Hope that's fine.",
    }
    return f"{styles.get(style, styles['polite'])}\n\nRegards,\n{name}"

@mcp.tool()
def apply_leave(employee_id: str, days: int, reason: str) -> str:
    """Apply leave for given employee if enough balance"""
    data = mock_leave_db.get(employee_id)
    if not data:
        return f"Employee ID '{employee_id}' not found."

    remaining = calculate_leave_balance(data["total_leaves"], data["used_leaves"])
    if days > remaining:
        return f"Insufficient balance. {data['name']} has only {remaining} leave(s) left."

    # Simulate leave application
    data["pending_requests"] += 1
    return (
        f"Leave request for {days} day(s) submitted successfully for {data['name']}.\n"
        f"Reason: {reason}\n"
        f"Pending Requests: {data['pending_requests']}"
    )

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a personalized greeting"""
    return f"Hello {name}, welcome to the Leave Management System!"

# Prompt: Greet User
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }
    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

# This is the crucial part that was missing proper formatting
if __name__ == "__main__":
    mcp.run()