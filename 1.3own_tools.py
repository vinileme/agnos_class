import os

from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openrouter import OpenRouter

def celcius_to_fh(temperatura_celcius: float):
    """
    Converte uma temperatura em graus Celsius para Fahrenheit.
    
    Args:
        temperatura_celsius (float): Temperatura em graus Celsius
        
    Return:
        float: Temperatura convertida em graus Fahrenheit
    """
    return (temperatura_celcius * 9/5) + 32


agent = Agent(
    model=OpenRouter(
        id="deepseek-v4.1-flash-1017",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    ),
    tools=[
        TavilyTools(),
        celcius_to_fh
    ],
 debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em São Paulo em Fahrenheit e fale a porcentagem de chance de chuva para hoje (07 de novembro de 2026)a tarde em taboão da serra")
