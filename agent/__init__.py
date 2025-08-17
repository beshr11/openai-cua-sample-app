from .agent import Agent
from .deep_researcher import DeepResearcherAgent
from .developer import DeveloperAgent
from .user_agent import UserAgent

# Agent registry for easy access
AGENT_TYPES = {
    "cua": Agent,
    "deep_researcher": DeepResearcherAgent,
    "developer": DeveloperAgent,
    "user": UserAgent
}
