import pytest
from agent import AGENT_TYPES


class TestAgentTypes:
    """Test all agent types are properly configured."""

    def test_all_agent_types_available(self):
        """Test that all expected agent types are available."""
        expected_types = ["cua", "deep_researcher", "developer", "user"]
        
        for agent_type in expected_types:
            assert agent_type in AGENT_TYPES, f"Agent type '{agent_type}' not found"

    @pytest.mark.parametrize("agent_type", AGENT_TYPES.keys())
    def test_agent_instantiation(self, agent_type):
        """Test that each agent type can be instantiated."""
        agent_class = AGENT_TYPES[agent_type]
        agent = agent_class()
        
        assert agent is not None
        assert hasattr(agent, 'model')
        assert hasattr(agent, 'tools')

    @pytest.mark.parametrize("agent_type", AGENT_TYPES.keys())
    def test_agent_has_required_methods(self, agent_type):
        """Test that each agent has required methods."""
        agent_class = AGENT_TYPES[agent_type]
        agent = agent_class()
        
        # Test required methods exist
        assert hasattr(agent, 'get_agent_type'), f"{agent_type} missing get_agent_type()"
        assert hasattr(agent, 'get_capabilities'), f"{agent_type} missing get_capabilities()"
        assert hasattr(agent, 'run_full_turn'), f"{agent_type} missing run_full_turn()"

    @pytest.mark.parametrize("agent_type", AGENT_TYPES.keys())
    def test_agent_type_method_returns_correct_value(self, agent_type):
        """Test that get_agent_type() returns the correct value."""
        agent_class = AGENT_TYPES[agent_type]
        agent = agent_class()
        
        returned_type = agent.get_agent_type()
        assert returned_type == agent_type, f"Expected '{agent_type}', got '{returned_type}'"

    @pytest.mark.parametrize("agent_type", AGENT_TYPES.keys())
    def test_agent_capabilities_not_empty(self, agent_type):
        """Test that each agent has capabilities defined."""
        agent_class = AGENT_TYPES[agent_type]
        agent = agent_class()
        
        capabilities = agent.get_capabilities()
        assert isinstance(capabilities, list), f"{agent_type} capabilities should be a list"
        assert len(capabilities) > 0, f"{agent_type} should have at least one capability"
        
        # Ensure all capabilities are strings
        for capability in capabilities:
            assert isinstance(capability, str), f"Capability should be string, got {type(capability)}"

    def test_specialized_agents_have_additional_tools(self):
        """Test that specialized agents have more tools than the base CUA agent."""
        base_agent = AGENT_TYPES["cua"]()
        base_tool_count = len(base_agent.tools)
        
        specialized_agents = ["deep_researcher", "developer", "user"]
        
        for agent_type in specialized_agents:
            agent = AGENT_TYPES[agent_type]()
            agent_tool_count = len(agent.tools)
            
            assert agent_tool_count > base_tool_count, \
                f"{agent_type} should have more tools than base CUA agent ({agent_tool_count} vs {base_tool_count})"

    def test_agent_tools_are_properly_formatted(self):
        """Test that agent tools are properly formatted."""
        for agent_type, agent_class in AGENT_TYPES.items():
            agent = agent_class()
            
            for tool in agent.tools:
                # Each tool should be a dictionary
                assert isinstance(tool, dict), f"{agent_type} tool should be dict"
                
                # Tool should have required fields
                if tool.get("type") == "function":
                    assert "function" in tool, f"{agent_type} function tool missing 'function' field"
                    func = tool["function"]
                    assert "name" in func, f"{agent_type} function missing 'name'"
                    assert "description" in func, f"{agent_type} function missing 'description'"
                    assert "parameters" in func, f"{agent_type} function missing 'parameters'"

    def test_agent_inheritance(self):
        """Test that all agents inherit from the base Agent class."""
        from agent.agent import Agent
        
        for agent_type, agent_class in AGENT_TYPES.items():
            assert issubclass(agent_class, Agent), f"{agent_type} should inherit from Agent"