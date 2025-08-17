"""
User Agent - Specialized for general user assistance and task automation.
"""
from .agent import Agent
from computers import Computer
from typing import Callable


class UserAgent(Agent):
    """
    A specialized agent optimized for general user assistance and task automation.
    
    This agent extends the base CUA functionality with user-focused capabilities
    such as personal productivity, task management, and general computer usage assistance.
    """
    
    def __init__(
        self,
        model="computer-use-preview",
        computer: Computer = None,
        tools: list[dict] = [],
        acknowledge_safety_check_callback: Callable = lambda: False,
    ):
        # Add user assistance-specific tools and configuration
        user_tools = [
            {
                "type": "function",
                "function": {
                    "name": "manage_tasks",
                    "description": "Help manage and organize user tasks and schedules",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "action": {"type": "string", "enum": ["create", "update", "delete", "list"]},
                            "task_description": {"type": "string", "description": "Task description"},
                            "priority": {"type": "string", "enum": ["low", "medium", "high"]},
                            "due_date": {"type": "string", "description": "Due date in YYYY-MM-DD format"}
                        },
                        "required": ["action"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "automate_workflow",
                    "description": "Automate repetitive user workflows and tasks",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "workflow_type": {"type": "string", "description": "Type of workflow to automate"},
                            "steps": {"type": "array", "items": {"type": "string"}, "description": "Workflow steps"},
                            "schedule": {"type": "string", "description": "When to run the workflow"}
                        },
                        "required": ["workflow_type", "steps"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "organize_files",
                    "description": "Help organize and manage user files and folders",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "directory": {"type": "string", "description": "Directory to organize"},
                            "criteria": {"type": "string", "description": "Organization criteria (date, type, name)"},
                            "action": {"type": "string", "enum": ["sort", "clean", "backup"]}
                        },
                        "required": ["directory", "action"]
                    }
                }
            }
        ]
        
        # Combine user tools with provided tools
        combined_tools = tools + user_tools
        
        super().__init__(
            model=model,
            computer=computer,
            tools=combined_tools,
            acknowledge_safety_check_callback=acknowledge_safety_check_callback
        )
        
        # User assistance-specific configuration  
        self.user_assistance_mode = True
        self.productivity_focus = True
        
    def get_agent_type(self):
        """Return the agent type identifier."""
        return "user"
        
    def get_capabilities(self):
        """Return list of agent capabilities."""
        return [
            "Personal productivity assistance",
            "Task and schedule management",
            "Workflow automation",
            "File and data organization", 
            "General computer usage help",
            "Application assistance",
            "Digital life management"
        ]