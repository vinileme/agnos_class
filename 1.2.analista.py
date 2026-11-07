from agno.agent import Agent, agent    
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[YFinanceTools()],
    #debug_mode=True
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)

agent.print_response("Qual é a cotação da apple hoje?", stream=True)

