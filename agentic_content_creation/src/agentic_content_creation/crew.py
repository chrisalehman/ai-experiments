import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from pydantic import BaseModel, Field
from typing import List
from agentic_content_creation.env_helper import get_value

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


class SocialMediaPost(BaseModel):
    platform: str = Field(..., description="The social media platform where the post will be published (e.g., Twitter, LinkedIn).")
    content: str = Field(..., description="The content of the social media post, including any hashtags or mentions.")

class ContentOutput(BaseModel):
    article: str = Field(..., description="The article, formatted in markdown.")
    social_media_posts: List[SocialMediaPost] = Field(..., description="A list of social media posts related to the article.")

@CrewBase
class AgenticContentCreation():
	"""ContentBot crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	## TOOLS & CONFIG ##
	serperApiKey = get_value('SERPER_API_KEY')	
	print(f"*****SERPER_API_KEY: {serperApiKey}")

	os.environ["SERPER_API_KEY"] = get_value('SERPER_API_KEY')
	serper = SerperDevTool()
	scraper = ScrapeWebsiteTool()
	searcher = WebsiteSearchTool()


	## AGENTS ##
	
	@agent
	def market_news_monitor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['market_news_monitor_agent'],
			tools=[self.serper, self.scraper],
		)

	@agent
	def data_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst_agent'],
			tools=[self.serper, self.searcher],
		)

	@agent
	def content_creator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['content_creator_agent'],
			tools=[self.serper, self.scraper],
		)

	@agent
	def quality_assurance_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['quality_assurance_agent'],
		)

	# TASKS ##

	@task
	def monitor_market_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['monitor_market_news_task'],
		)

	@task
	def analyze_market_data_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_market_data_task'],
		)

	@task
	def create_content_task(self) -> Task:
		return Task(
			config=self.tasks_config['create_content_task'],
			# context=[self.monitor_market_news_task, self.analyze_market_data_task]
		)

	@task
	def quality_assurance_task(self) -> Task:
		return Task(
			config=self.tasks_config['quality_assurance_task'],
			output_pydantic=ContentOutput,
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ContentBot crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)