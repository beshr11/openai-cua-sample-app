#!/usr/bin/env python3
"""
Installation and Configuration Script for OpenAI CUA Multi-Agent System

This script installs and configures the CUA, Deep Researcher, Developer, and User agents
ensuring a complete and fully functional setup for each agent.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import argparse

def print_step(message):
    """Print a formatted step message."""
    print(f"\n{'='*60}")
    print(f"STEP: {message}")
    print(f"{'='*60}")

def print_success(message):
    """Print a formatted success message."""
    print(f"✅ SUCCESS: {message}")

def print_error(message):
    """Print a formatted error message."""
    print(f"❌ ERROR: {message}")

def print_info(message):
    """Print a formatted info message."""
    print(f"ℹ️  INFO: {message}")

def check_python_version():
    """Check if Python version is compatible."""
    print_step("Checking Python Version")
    
    if sys.version_info < (3, 8):
        print_error("Python 3.8 or higher is required.")
        return False
    
    print_success(f"Python {sys.version.split()[0]} detected")
    return True

def setup_virtual_environment():
    """Create and activate virtual environment."""
    print_step("Setting Up Virtual Environment")
    
    venv_path = Path(".venv")
    
    if venv_path.exists():
        print_info("Virtual environment already exists")
    else:
        try:
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
            print_success("Virtual environment created")
        except subprocess.CalledProcessError:
            print_error("Failed to create virtual environment")
            return False
    
    # Check if activation works
    if os.name == "nt":  # Windows
        activate_script = venv_path / "Scripts" / "activate.bat"
    else:  # Unix/Linux/Mac
        activate_script = venv_path / "bin" / "activate"
    
    if activate_script.exists():
        print_success("Virtual environment setup complete")
        return True
    else:
        print_error("Virtual environment activation script not found")
        return False

def install_dependencies():
    """Install required dependencies."""
    print_step("Installing Dependencies")
    
    # Determine pip path
    if os.name == "nt":  # Windows
        pip_path = Path(".venv") / "Scripts" / "pip"
    else:  # Unix/Linux/Mac
        pip_path = Path(".venv") / "bin" / "pip"
    
    try:
        # Install main requirements
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
        print_success("Main dependencies installed")
        
        # Install additional testing dependencies
        subprocess.run([str(pip_path), "install", "pytest", "pytest-cov"], check=True)
        print_success("Testing dependencies installed")
        
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False

def install_playwright_browsers():
    """Install Playwright browser dependencies."""
    print_step("Installing Playwright Browsers")
    
    # Determine python path
    if os.name == "nt":  # Windows
        python_path = Path(".venv") / "Scripts" / "python"
    else:  # Unix/Linux/Mac
        python_path = Path(".venv") / "bin" / "python"
    
    try:
        subprocess.run([str(python_path), "-m", "playwright", "install"], check=True)
        print_success("Playwright browsers installed")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install Playwright browsers: {e}")
        print_info("You may need to run 'playwright install' manually later")
        return True  # Don't fail installation for this

def setup_environment_file():
    """Set up environment configuration file."""
    print_step("Setting Up Environment Configuration")
    
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print_info(".env file already exists")
        return True
    
    if env_example.exists():
        try:
            shutil.copy(env_example, env_file)
            print_success(".env file created from template")
            print_info("Please edit .env file with your API keys:")
            print_info("  - OPENAI_API_KEY")
            print_info("  - BROWSERBASE_API_KEY (optional)")
            print_info("  - SCRAPYBARA_API_KEY (optional)")
            return True
        except Exception as e:
            print_error(f"Failed to create .env file: {e}")
            return False
    else:
        print_error(".env.example template not found")
        return False

def validate_agent_installation(agent_type):
    """Validate that a specific agent can be imported and instantiated."""
    print_info(f"Validating {agent_type} agent...")
    
    # Determine python path
    if os.name == "nt":  # Windows
        python_path = Path(".venv") / "Scripts" / "python"
    else:  # Unix/Linux/Mac
        python_path = Path(".venv") / "bin" / "python"
    
    validation_script = f"""
import sys
sys.path.insert(0, '.')

try:
    from agent import AGENT_TYPES
    
    agent_class = AGENT_TYPES.get('{agent_type}')
    if agent_class is None:
        print(f"ERROR: Agent type '{agent_type}' not found")
        sys.exit(1)
    
    # Test basic instantiation (without computer for now)
    agent = agent_class()
    print(f"SUCCESS: {agent_type} agent can be instantiated")
    
    # Test agent type method
    if hasattr(agent, 'get_agent_type'):
        actual_agent_type = agent.get_agent_type()
        print(f"SUCCESS: Agent type: {{actual_agent_type}}")
    
    # Test capabilities method
    if hasattr(agent, 'get_capabilities'):
        capabilities = agent.get_capabilities()
        print(f"SUCCESS: Agent capabilities: {{len(capabilities)}} items")
        
except Exception as e:
    print(f"ERROR: {{e}}")
    sys.exit(1)
"""
    
    try:
        result = subprocess.run(
            [str(python_path), "-c", validation_script],
            capture_output=True,
            text=True,
            check=True
        )
        print_success(f"{agent_type} agent validation passed")
        if result.stdout:
            for line in result.stdout.strip().split('\n'):
                if line.startswith('SUCCESS:'):
                    print_info(line[8:])  # Remove SUCCESS: prefix
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"{agent_type} agent validation failed")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def run_tests():
    """Run the test suite to validate installation."""
    print_step("Running Test Suite")
    
    # Determine python path
    if os.name == "nt":  # Windows
        python_path = Path(".venv") / "Scripts" / "python"
    else:  # Unix/Linux/Mac
        python_path = Path(".venv") / "bin" / "python"
    
    try:
        result = subprocess.run(
            [str(python_path), "-m", "pytest", "tests/", "-v"],
            check=True,
            capture_output=True,
            text=True
        )
        print_success("All tests passed")
        return True
    except subprocess.CalledProcessError as e:
        print_error("Some tests failed")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def print_installation_summary():
    """Print installation summary and next steps."""
    print_step("Installation Complete")
    
    print("🎉 All agents have been successfully installed and configured!")
    print()
    print("AVAILABLE AGENTS:")
    print("  • CUA (Computer Using Agent) - Base computer control agent")
    print("  • Deep Researcher - Specialized for research and information gathering")
    print("  • Developer - Specialized for software development tasks")
    print("  • User - Specialized for general user assistance and task automation")
    print()
    print("NEXT STEPS:")
    print("1. Edit .env file with your OpenAI API key")
    print("2. Run an agent using the CLI:")
    print("   python cli.py --agent-type cua --computer local-playwright")
    print("   python cli.py --agent-type deep_researcher --computer local-playwright")
    print("   python cli.py --agent-type developer --computer local-playwright")
    print("   python cli.py --agent-type user --computer local-playwright")
    print()
    print("3. For more advanced usage, see the examples/ directory")
    print()
    print("VALIDATION COMMANDS:")
    print("   python -m pytest tests/  # Run all tests")
    print("   python validate_agents.py  # Validate all agent types")

def main():
    """Main installation function."""
    parser = argparse.ArgumentParser(description="Install and configure CUA multi-agent system")
    parser.add_argument("--skip-browsers", action="store_true", 
                       help="Skip Playwright browser installation")
    parser.add_argument("--skip-tests", action="store_true",
                       help="Skip running tests during installation")
    args = parser.parse_args()
    
    print("🚀 OpenAI CUA Multi-Agent System Installation")
    print("=" * 60)
    
    # Installation steps
    steps = [
        ("Check Python Version", check_python_version),
        ("Setup Virtual Environment", setup_virtual_environment),
        ("Install Dependencies", install_dependencies),
        ("Setup Environment File", setup_environment_file),
    ]
    
    if not args.skip_browsers:
        steps.append(("Install Playwright Browsers", install_playwright_browsers))
    
    # Execute installation steps
    for step_name, step_func in steps:
        if not step_func():
            print_error(f"Installation failed at step: {step_name}")
            sys.exit(1)
    
    # Validate all agent types
    print_step("Validating Agent Installations")
    agent_types = ["cua", "deep_researcher", "developer", "user"]
    
    for agent_type in agent_types:
        if not validate_agent_installation(agent_type):
            print_error(f"Agent validation failed for: {agent_type}")
            sys.exit(1)
    
    # Run tests if not skipped
    if not args.skip_tests:
        if not run_tests():
            print_error("Test validation failed")
            sys.exit(1)
    
    # Print summary
    print_installation_summary()

if __name__ == "__main__":
    main()