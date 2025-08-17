"""
Developer Agent - Specialized for software development tasks.
"""
from .agent import Agent
from computers import Computer
from typing import Callable


class DeveloperAgent(Agent):
    """
    A specialized agent optimized for software development tasks.
    
    This agent extends the base CUA functionality with development-specific capabilities
    such as code analysis, debugging, testing, and development environment management.
    """
    
    def __init__(
        self,
        model="computer-use-preview", 
        computer: Computer = None,
        tools: list[dict] = [],
        acknowledge_safety_check_callback: Callable = lambda: False,
    ):
        # Add development-specific tools and configuration
        dev_tools = [
            {
                "type": "function",
                "function": {
                    "name": "analyze_code",
                    "description": "Analyze code for bugs, performance issues, and best practices",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string", "description": "Path to the code file"},
                            "language": {"type": "string", "description": "Programming language"},
                            "analysis_type": {"type": "string", "enum": ["bugs", "performance", "style", "security"]}
                        },
                        "required": ["file_path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "run_tests",
                    "description": "Execute test suites and analyze results",
                    "parameters": {
                        "type": "object", 
                        "properties": {
                            "test_path": {"type": "string", "description": "Path to test files or directory"},
                            "test_framework": {"type": "string", "description": "Testing framework to use"},
                            "coverage": {"type": "boolean", "description": "Generate coverage report"}
                        },
                        "required": ["test_path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "debug_application",
                    "description": "Debug application issues and provide solutions",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "error_log": {"type": "string", "description": "Error log or description"},
                            "context": {"type": "string", "description": "Application context"}
                        },
                        "required": ["error_log"]
                    }
                }
            }
        ]
        
        # Combine development tools with provided tools
        combined_tools = tools + dev_tools
        
        super().__init__(
            model=model,
            computer=computer,
            tools=combined_tools,
            acknowledge_safety_check_callback=acknowledge_safety_check_callback
        )
        
        # Development-specific configuration
        self.development_mode = True
        self.code_analysis_enabled = True
        
    def get_agent_type(self):
        """Return the agent type identifier."""
        return "developer"
        
    def get_capabilities(self):
        """Return list of agent capabilities."""
        return [
            "Code analysis and review",
            "Automated testing and debugging", 
            "Development environment setup",
            "Version control operations",
            "Build and deployment assistance",
            "Performance optimization",
            "Security analysis"
        ]