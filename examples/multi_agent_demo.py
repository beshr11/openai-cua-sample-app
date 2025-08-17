#!/usr/bin/env python3
"""
Multi-Agent Example - Demonstrates all four agent types
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import AGENT_TYPES


def demonstrate_agent(agent_type, task_description):
    """Demonstrate a specific agent type with a sample task."""
    print(f"\n{'='*60}")
    print(f"Demonstrating {agent_type.upper()} Agent")
    print(f"{'='*60}")
    
    try:
        # Create agent without computer for demonstration
        agent = AGENT_TYPES[agent_type]()
        
        print(f"Agent Type: {agent.get_agent_type()}")
        print(f"Task: {task_description}")
        print("\nCapabilities:")
        
        capabilities = agent.get_capabilities()
        for i, capability in enumerate(capabilities, 1):
            print(f"  {i}. {capability}")
        
        print(f"\nSpecialized Tools: {len(agent.tools)} available")
        if agent.tools:
            for tool in agent.tools:
                if 'function' in tool:
                    func_name = tool['function']['name']
                    func_desc = tool['function']['description']
                    print(f"  • {func_name}: {func_desc}")
        
        print("✅ Agent demonstration successful")
        
    except Exception as e:
        print(f"❌ Error demonstrating {agent_type}: {e}")


def main():
    """Main demonstration function."""
    print("🤖 OpenAI CUA Multi-Agent System Demonstration")
    print("=" * 60)
    
    # Define demonstration tasks for each agent type
    demonstrations = {
        "cua": "Control a web browser to navigate and interact with websites",
        "deep_researcher": "Research the latest developments in artificial intelligence",
        "developer": "Analyze a Python codebase and identify potential improvements",  
        "user": "Organize files and automate daily productivity tasks"
    }
    
    # Demonstrate each agent type
    for agent_type, task in demonstrations.items():
        demonstrate_agent(agent_type, task)
    
    print(f"\n{'='*60}")
    print("🎉 All agent demonstrations completed successfully!")
    print("=" * 60)
    
    print("\nTo run agents interactively:")
    print("  python cli.py --agent-type cua")
    print("  python cli.py --agent-type deep_researcher") 
    print("  python cli.py --agent-type developer")
    print("  python cli.py --agent-type user")
    
    print("\nFor detailed usage information:")
    print("  python cli.py --help")
    print("  cat AGENT_INSTALLATION_GUIDE.md")


if __name__ == "__main__":
    main()