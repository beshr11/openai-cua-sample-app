# Installation and Configuration Checklist

## Quick Installation Checklist

- [x] **Set up environment** - Python 3.8+ with virtual environment
- [x] **Install dependencies** - All required packages from requirements.txt  
- [x] **Install specialized agents** - CUA, Deep Researcher, Developer, User agents
- [x] **Configure environment** - Set up .env file with API keys
- [x] **Validate installation** - All agents working and tested
- [x] **Enable full functionality** - All configuration options enabled
- [x] **Provide clear commands** - Step-by-step installation and usage

## Installation Commands

### 1. Automated Installation (Recommended)

```bash
# Download and run the automated installer
python install_agents.py

# Or skip browser installation if needed
python install_agents.py --skip-browsers

# Or skip tests during installation
python install_agents.py --skip-tests
```

### 2. Manual Installation

```bash
# Step 1: Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Step 2: Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Step 3: Install Playwright browsers (for browser automation)
python -m playwright install

# Step 4: Set up environment configuration
cp .env.example .env
# Edit .env file with your API keys
```

### 3. Configuration Setup

```bash
# Edit environment file with your credentials
nano .env  # or use your preferred editor

# Required:
OPENAI_API_KEY="sk-proj-your-key-here"

# Optional (for remote browser environments):
BROWSERBASE_API_KEY="your-browserbase-key"
SCRAPYBARA_API_KEY="your-scrapybara-key"
```

## Validation Commands

### Validate All Agents

```bash
# Run comprehensive agent validation
python validate_agents.py

# Run all tests
python -m pytest tests/ -v

# Run specific agent tests
python -m pytest tests/test_agents.py -v
```

### Test Individual Agents

```bash
# Test CUA agent
python cli.py --agent-type cua --help

# Test Deep Researcher agent  
python cli.py --agent-type deep_researcher --help

# Test Developer agent
python cli.py --agent-type developer --help

# Test User agent
python cli.py --agent-type user --help
```

## Usage Commands

### Run Agents Interactively

```bash
# Run CUA agent (base computer control)
python cli.py --agent-type cua --computer local-playwright

# Run Deep Researcher agent (research and information gathering)
python cli.py --agent-type deep_researcher --computer local-playwright

# Run Developer agent (software development tasks)
python cli.py --agent-type developer --computer local-playwright  

# Run User agent (general user assistance)
python cli.py --agent-type user --computer local-playwright
```

### Advanced Usage Options

```bash
# Run with debug mode and show images
python cli.py --agent-type developer --debug --show

# Start with specific URL
python cli.py --agent-type deep_researcher --start-url "https://arxiv.org"

# Run with initial input
python cli.py --agent-type user --input "Help me organize my files"

# Use different computer environments
python cli.py --agent-type cua --computer docker
python cli.py --agent-type cua --computer browserbase  # requires API key
python cli.py --agent-type cua --computer scrapybara-browser  # requires API key
```

## Verification Steps

### Post-Installation Validation

1. **Environment Check**
   ```bash
   python --version  # Should be 3.8+
   source .venv/bin/activate
   pip list | grep -E "(playwright|openai|pydantic)"
   ```

2. **Agent Import Test**
   ```bash
   python -c "from agent import AGENT_TYPES; print(list(AGENT_TYPES.keys()))"
   # Should output: ['cua', 'deep_researcher', 'developer', 'user']
   ```

3. **Agent Instantiation Test**
   ```bash
   python -c "from agent import AGENT_TYPES; [AGENT_TYPES[t]() for t in AGENT_TYPES]"
   # Should complete without errors
   ```

4. **Capabilities Test**
   ```bash
   python examples/multi_agent_demo.py
   # Should show all agent capabilities
   ```

5. **Full Test Suite**
   ```bash
   python -m pytest tests/ -v
   # Should pass all 25+ tests
   ```

## Success Indicators

✅ **Installation Complete** when:
- All dependencies installed without errors
- Virtual environment activated successfully  
- All 4 agent types can be imported and instantiated
- CLI shows all agent types in help output
- Validation script reports all agents as working
- Test suite passes all tests

✅ **Configuration Complete** when:
- .env file exists with API keys
- Agent type selection works in CLI
- Each agent shows correct capabilities
- Specialized tools are available for each agent type

✅ **Full Functionality Enabled** when:
- All computer environments can be selected
- Browser automation works (if Playwright installed)
- Debug mode and image display work
- All specialized agent features are accessible

## Troubleshooting Commands

```bash
# Check installation status
python validate_agents.py

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Reinstall Playwright
python -m playwright install --force

# Check environment variables
python -c "import os; print([k for k in os.environ.keys() if 'API' in k])"

# Test basic agent functionality
python -c "from agent import AGENT_TYPES; print(AGENT_TYPES['cua']().get_capabilities())"
```

## Quick Demo Commands

```bash
# Quick demonstration of all agents
python examples/multi_agent_demo.py

# Interactive session with each agent type
python cli.py --agent-type deep_researcher --input "What are the latest AI developments?"
python cli.py --agent-type developer --input "Analyze this code for improvements"  
python cli.py --agent-type user --input "Help me with file organization"
```