from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AuditReportWritingCrew():
	"""AuditReportWritingCrew crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	llm = LLM(model="ollama/llama3")

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def ai_finding_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_finding_writer'],
			verbose=True,
			llm=self.llm,
		)

	@agent
	def gia_ai_finding_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['gia_ai_finding_writer'],
			verbose=True,
			llm=self.llm,
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_finding_writing_task'],
			output_file='finding.md',
			llm = self.llm,
			
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['gia_ai_finding_writing_task'],
			output_file='gia_finding.md',
			llm=self.llm,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AuditReportWritingCrew crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			llm=self.llm,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)