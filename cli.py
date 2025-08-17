import argparse
from agent import AGENT_TYPES
from computers.config import *
from computers.default import *
from computers import computers_config


def acknowledge_safety_check_callback(message: str) -> bool:
    response = input(
        f"Safety Check Warning: {message}\nDo you want to acknowledge and proceed? (y/n): "
    ).lower()
    return response.lower().strip() == "y"


def main():
    parser = argparse.ArgumentParser(
        description="OpenAI CUA Multi-Agent System - Select agent type and computer environment."
    )
    parser.add_argument(
        "--agent-type",
        choices=AGENT_TYPES.keys(),
        help="Choose the agent type to use.",
        default="cua",
    )
    parser.add_argument(
        "--computer",
        choices=computers_config.keys(),
        help="Choose the computer environment to use.",
        default="local-playwright",
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Initial input to use instead of asking the user.",
        default=None,
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode for detailed output.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show images during the execution.",
    )
    parser.add_argument(
        "--start-url",
        type=str,
        help="Start the browsing session with a specific URL (only for browser environments).",
        default="https://bing.com",
    )
    args = parser.parse_args()
    
    # Get the appropriate agent and computer classes
    AgentClass = AGENT_TYPES[args.agent_type]
    ComputerClass = computers_config[args.computer]
    
    # Print agent information
    print(f"🤖 Starting {args.agent_type.upper()} Agent")
    print(f"💻 Using {args.computer} computer environment")
    
    # Create a temporary agent to show capabilities
    temp_agent = AgentClass()
    if hasattr(temp_agent, 'get_capabilities'):
        capabilities = temp_agent.get_capabilities()
        print(f"🎯 Agent Capabilities:")
        for i, capability in enumerate(capabilities, 1):
            print(f"   {i}. {capability}")
    print()

    with ComputerClass() as computer:
        agent = AgentClass(
            computer=computer,
            acknowledge_safety_check_callback=acknowledge_safety_check_callback,
        )
        items = []

        if args.computer in ["browserbase", "local-playwright"]:
            if not args.start_url.startswith("http"):
                args.start_url = "https://" + args.start_url
            agent.computer.goto(args.start_url)

        while True:
            try:
                user_input = args.input or input("> ")
                if user_input == "exit":
                    break
            except EOFError as e:
                print(f"An error occurred: {e}")
                break
            items.append({"role": "user", "content": user_input})
            output_items = agent.run_full_turn(
                items,
                print_steps=True,
                show_images=args.show,
                debug=args.debug,
            )
            items += output_items
            args.input = None


if __name__ == "__main__":
    main()
