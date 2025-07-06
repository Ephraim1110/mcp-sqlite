from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from gradio_client import Client

# MCP URL Gradio
MCP_URL = "http://127.0.0.1:7860"

# Création du client Gradio
client = Client(MCP_URL)

def afficher_users(_):
    # Appelle la fonction Gradio "afficher_users"
    return client.predict(api_name="/afficher_users")

def get_db_schema(_):
    # Appelle la fonction Gradio "get_db_schema_info"
    return client.predict(api_name="/get_db_schema_info")

# Déclaration des tools LangChain
tools = [
    Tool(
        name="AfficherUsers",
        func=afficher_users,
        description="Affiche tous les utilisateurs de la base."
    ),
    Tool(
        name="GetDBSchema",
        func=get_db_schema,
        description="Affiche le schéma de la base de données."
    )
]

# LLM local avec Ollama
llm = ChatOllama(model="qwen2.5")

# Initialisation de l'agent LangChain
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    while True:
        query = input("Pose ta question : ")
        if query.lower() in ["exit", "quit"]:
            break
        print(agent.run(query))
