import gradio as gr
import sqlite3 
connection = sqlite3.connect("test.db")

#creer la  table 
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)") ;
cursor.execute("INSERT INTO users VALUES (1, 'alice', 20)")
cursor.execute("INSERT INTO users VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO users VALUES (3, 'eve', 40)")
connection.commit()

def afficher_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return {"users": users}

with gr.Blocks() as demo:
    gr.Markdown("# MCP Server BDD")
    btn = gr.Button("Afficher users")
    output = gr.Textbox()
    btn.click(afficher_users, outputs=output)

if __name__ == "__main__":
    demo.launch(mcp_server=True)
