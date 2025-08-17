#!/usr/bin/env python3
"""
Agent Validation Script

This script validates that all agent types are properly installed and configured.
"""

import sys
from pathlib import Path

def validate_agent(agent_type, agent_class):
    """Validate a specific agent type."""
    print(f"\n{'='*50}")
    print(f"Validating {agent_type.upper()} Agent")
    print(f"{'='*50}")
    
    try:
        # Test basic instantiation
        agent = agent_class()
        print(f"✅ {agent_type} agent instantiation successful")
        
        # Test agent type method
        if hasattr(agent, 'get_agent_type'):
            actual_type = agent.get_agent_type()
            print(f"✅ Agent type: {actual_type}")
            
            if actual_type != agent_type:
                print(f"⚠️  Warning: Expected '{agent_type}' but got '{actual_type}'")
        else:
            print(f"⚠️  Warning: get_agent_type() method not found")
        
        # Test capabilities method
        if hasattr(agent, 'get_capabilities'):
            capabilities = agent.get_capabilities()
            print(f"✅ Agent capabilities ({len(capabilities)} items):")
            for i, capability in enumerate(capabilities, 1):
                print(f"   {i}. {capability}")
        else:
            print(f"⚠️  Warning: get_capabilities() method not found")
        
        # Test tools configuration
        if hasattr(agent, 'tools'):
            tool_count = len(agent.tools)
            print(f"✅ Tools configured: {tool_count} tools available")
        else:
            print(f"⚠️  Warning: tools attribute not found")
        
        print(f"✅ {agent_type} agent validation PASSED")
        return True
        
    except Exception as e:
        print(f"❌ {agent_type} agent validation FAILED: {e}")
        return False

def main():
    """Main validation function."""
    print("🔍 OpenAI CUA Multi-Agent System Validation")
    print("=" * 60)
    
    try:
        # Import agent types
        from agent import AGENT_TYPES
        print("✅ Agent module imports successful")
        
        # Validate each agent type
        all_passed = True
        results = {}
        
        for agent_type, agent_class in AGENT_TYPES.items():
            success = validate_agent(agent_type, agent_class)
            results[agent_type] = success
            if not success:
                all_passed = False
        
        # Print summary
        print(f"\n{'='*60}")
        print("VALIDATION SUMMARY")
        print(f"{'='*60}")
        
        for agent_type, success in results.items():
            status = "PASSED" if success else "FAILED"
            emoji = "✅" if success else "❌"
            print(f"{emoji} {agent_type.upper()} Agent: {status}")
        
        if all_passed:
            print(f"\n🎉 ALL AGENTS VALIDATED SUCCESSFULLY!")
            print("The multi-agent system is ready for use.")
            return 0
        else:
            print(f"\n❌ SOME AGENTS FAILED VALIDATION")
            print("Please check the error messages above and fix any issues.")
            return 1
            
    except ImportError as e:
        print(f"❌ Failed to import agent modules: {e}")
        print("Please ensure the installation completed successfully.")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error during validation: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())