# AgenticContentCreation Crew

This project provides a simple example of a multi-agent system for developing a report and social media posts utilizing Crew AI. This project uses GPT-4 as the default LLM for the agents. 

The agents involved in this example are as follows: 
- Lead Bitcoin Market Analyst: for researching current market news related to Bitcoin
- Senior Bitcoin Data Strategist: for synthesizing the research by the Market News agent
- Senior Bitcoin Content Director: for developing the content
- Chief Bitcoin Content Officer: for assembling, editing and validating content created by the Content Director agent.

In addition, the agents use the following tools: 
- Serper Dev Tool: for searching the web through Google's Search API. 
- Scrape Website Tool: for extrating data from a specific URL
- Website Search Tool: for performing a semantic search within the scraped content

The result is a `report.md` of the generated content (as well as output to standard out).

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience. It is recommended that you install these packages in a virtual environment (see ../bin/venv.sh for details).

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your keys into the `.env` file**

- Convert the `.example.env` file to `.env` and add your own keys for Serper API and OpenAI. 

## Running the Project

To execute, run the following command from the root folder of your project:

```bash
$ crewai run
```

This command initializes the agentic-content-creation Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example will create a `report.md` file with the output of a research on Bitcoin in the root folder.

## Understanding Your Crew

The agentic-content-creation Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in the crew.