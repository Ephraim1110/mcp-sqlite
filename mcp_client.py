from gradio_client import Client


client = Client("http://127.0.0.1:7860/")

# Tester ton seul tool : afficher_users
result = client.predict(api_name="/afficher_users")

print("Résultat MCP Server :", result)
