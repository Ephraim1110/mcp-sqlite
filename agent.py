# agent.py

from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import StructuredTool
from gradio_client import Client

# MCP Client setup
mcp = Client("http://127.0.0.1:7860/")

def afficher_users():
    return mcp.predict(api_name="/afficher_users")

# Define the tool
afficher_users_tool = StructuredTool.from_function(
    name="afficher_users",
    description="Affiche la liste des utilisateurs SQLite via MCP.",
    func=afficher_users
)

# Initialize LLM with system prompt to encourage tool usage
llm = ChatOllama(
    model="gemma:3b",
    base_url="http://localhost:11434",
    system_message="Tu es un assistant qui répond uniquement via les outils fournis. Pour toute question concernant les utilisateurs, utilise l'outil 'afficher_users'."
)

# Initialize the agent
agent_executor = initialize_agent(
    tools=[afficher_users_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Interaction loop
if __name__ == "__main__":
    while True:
        question = input("Pose ta question : ")
        answer = agent_executor.run(question)
        print("\nRéponse :", answer)
