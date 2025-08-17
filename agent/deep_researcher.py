"""
Deep Researcher Agent - Specialized for research and information gathering tasks.
"""
from .agent import Agent
from computers import Computer
from typing import Callable


class DeepResearcherAgent(Agent):
    """
    A specialized agent optimized for research and information gathering tasks.
    
    This agent extends the base CUA functionality with research-specific capabilities
    such as systematic web browsing, information extraction, and knowledge synthesis.
    """
    
    def __init__(
        self,
        model="computer-use-preview",
        computer: Computer = None,
        tools: list[dict] = [],
        acknowledge_safety_check_callback: Callable = lambda: False,
    ):
        # Add research-specific tools and configuration
        research_tools = [
            {
                "type": "function",
                "function": {
                    "name": "search_web",
                    "description": "Search the web for information on a given topic",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "Search query"},
                            "max_results": {"type": "integer", "description": "Maximum number of results to return"}
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function", 
                "function": {
                    "name": "extract_information",
                    "description": "Extract key information from web pages or documents",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "source": {"type": "string", "description": "Source URL or document"},
                            "focus": {"type": "string", "description": "Specific information to focus on"}
                        },
                        "required": ["source"]
                    }
                }
            }
        ]
        
        # Combine research tools with provided tools
        combined_tools = tools + research_tools
        
        super().__init__(
            model=model,
            computer=computer,
            tools=combined_tools,
            acknowledge_safety_check_callback=acknowledge_safety_check_callback
        )
        
        # Research-specific configuration
        self.research_mode = True
        self.systematic_browsing = True
        
    def get_agent_type(self):
        """Return the agent type identifier."""
        return "deep_researcher"
        
    def get_capabilities(self):
        """Return list of agent capabilities."""
        return [
            "Web research and information gathering",
            "Systematic browsing and navigation", 
            "Information extraction and synthesis",
            "Multi-source verification",
            "Research documentation"
        ]