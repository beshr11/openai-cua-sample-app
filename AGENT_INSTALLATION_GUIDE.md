# Agent Installation and Configuration Guide

## Overview

This repository now supports four specialized agent types, each optimized for different tasks:

1. **CUA (Computer Using Agent)** - Base computer control agent
2. **Deep Researcher** - Specialized for research and information gathering  
3. **Developer** - Specialized for software development tasks
4. **User** - Specialized for general user assistance and task automation

## Quick Installation

### 1. Automated Installation (Recommended)

Run the automated installation script:

```bash
python install_agents.py
```

This will:
- Check Python version compatibility
- Set up virtual environment
- Install all dependencies  
- Install Playwright browsers
- Set up environment configuration
- Validate all agent installations
- Run test suite

### 2. Manual Installation

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Install Playwright browsers
python -m playwright install

# Set up environment file
cp .env.example .env
# Edit .env with your API keys
```

## Configuration

### Environment Variables

Edit `.env` file with your API keys:

```bash
OPENAI_API_KEY="sk-proj-your-key-here"
OPENAI_ORG="org-your-org-here"

# Optional: For remote browser environments
BROWSERBASE_API_KEY="your-browserbase-key"
BROWSERBASE_PROJECT_ID="your-project-id"
SCRAPYBARA_API_KEY="your-scrapybara-key"
```

### Agent-Specific Configuration

Each agent comes with specialized tools and capabilities:

#### CUA Agent (Base)
- Computer screen analysis and interaction
- Mouse and keyboard automation  
- Web browsing and navigation
- Application control and automation
- Screenshot analysis and decision making

#### Deep Researcher Agent
- Web research and information gathering
- Systematic browsing and navigation
- Information extraction and synthesis
- Multi-source verification
- Research documentation

**Additional Tools:**
- `search_web` - Search the web for information
- `extract_information` - Extract key information from web pages

#### Developer Agent  
- Code analysis and review
- Automated testing and debugging
- Development environment setup
- Version control operations
- Build and deployment assistance
- Performance optimization
- Security analysis

**Additional Tools:**
- `analyze_code` - Analyze code for bugs and best practices
- `run_tests` - Execute test suites
- `debug_application` - Debug application issues

#### User Agent
- Personal productivity assistance
- Task and schedule management
- Workflow automation
- File and data organization
- General computer usage help
- Application assistance
- Digital life management

**Additional Tools:**
- `manage_tasks` - Task and schedule management
- `automate_workflow` - Automate repetitive workflows
- `organize_files` - File and folder organization

## Usage

### Command Line Interface

The CLI now supports agent type selection:

```bash
# Run CUA agent (default)
python cli.py --agent-type cua --computer local-playwright

# Run Deep Researcher agent
python cli.py --agent-type deep_researcher --computer local-playwright

# Run Developer agent  
python cli.py --agent-type developer --computer local-playwright

# Run User agent
python cli.py --agent-type user --computer local-playwright
```

### Available Computer Environments

- `local-playwright` - Local browser automation (default)
- `docker` - Containerized desktop environment
- `browserbase` - Remote browser service (requires API key)
- `scrapybara-browser` - Remote browser via Scrapybara (requires API key)
- `scrapybara-ubuntu` - Remote Ubuntu desktop via Scrapybara (requires API key)

### Additional CLI Options

```bash
python cli.py \
  --agent-type developer \
  --computer local-playwright \
  --start-url "https://github.com" \
  --debug \
  --show \
  --input "Help me analyze this repository"
```

## Validation

### Validate Installation

Check that all agents are properly installed:

```bash
python validate_agents.py
```

### Run Tests

```bash
python -m pytest tests/ -v
```

### Test Individual Agents

```python
from agent import AGENT_TYPES

# Test Deep Researcher agent
researcher = AGENT_TYPES['deep_researcher']()
print(researcher.get_capabilities())

# Test Developer agent
developer = AGENT_TYPES['developer']()
print(developer.get_capabilities())

# Test User agent  
user_agent = AGENT_TYPES['user']()
print(user_agent.get_capabilities())
```

## Examples

### Research Task Example

```bash
python cli.py --agent-type deep_researcher --input "Research the latest developments in AI safety"
```

### Development Task Example

```bash
python cli.py --agent-type developer --input "Analyze this Python codebase for potential security issues"
```

### User Assistance Example

```bash
python cli.py --agent-type user --input "Help me organize my Downloads folder by file type"
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated
2. **Missing Playwright**: Run `python -m playwright install`
3. **API key errors**: Check `.env` file configuration
4. **Permission errors**: Make scripts executable with `chmod +x`

### Validation Steps

After each installation step:

1. **Environment Setup**: Virtual environment created successfully
2. **Dependencies**: All packages installed without errors  
3. **Agent Import**: All agent types can be imported
4. **Agent Instantiation**: All agents can be created
5. **Method Availability**: All agents have required methods
6. **Tools Configuration**: Specialized tools are properly configured

### Getting Help

If you encounter issues:

1. Run the validation script: `python validate_agents.py`
2. Check the test suite: `python -m pytest tests/ -v`
3. Enable debug mode: `--debug` flag in CLI
4. Check environment variables in `.env` file

## Advanced Usage

### Custom Agent Development

You can create custom agents by extending the base `Agent` class:

```python
from agent.agent import Agent

class CustomAgent(Agent):
    def __init__(self, **kwargs):
        custom_tools = [
            # Define your custom tools here
        ]
        super().__init__(tools=custom_tools, **kwargs)
    
    def get_agent_type(self):
        return "custom"
    
    def get_capabilities(self):
        return ["Custom capability 1", "Custom capability 2"]
```

### Integration with Other Systems

The agents can be integrated into larger systems by importing and using them programmatically:

```python
from agent import AGENT_TYPES
from computers import LocalPlaywrightBrowser

with LocalPlaywrightBrowser() as computer:
    agent = AGENT_TYPES['developer'](computer=computer)
    
    items = [{"role": "user", "content": "Analyze this code"}]
    results = agent.run_full_turn(items)
```