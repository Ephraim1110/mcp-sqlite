import gradio as gr
import sqlite3

DATABASE_NAME = "test.db"

def init_db():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)")
        
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO users VALUES (1, 'alice', 20)")
            cursor.execute("INSERT INTO users VALUES (2, 'bob', 30)")
            cursor.execute("INSERT INTO users VALUES (3, 'eve', 40)")
            conn.commit()
    finally:
        if conn:
            conn.close()

init_db()

def afficher_users():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        if not users:
            return "Aucun utilisateur trouvé."
        
        formatted_users = ""
        for user_id, name, age in users:
            formatted_users += f"ID: {user_id}, Nom: {name}, Âge: {age}\n"
        
        return formatted_users
    finally:
        if conn:
            conn.close()

with gr.Blocks() as demo:
    gr.Markdown("# MCP Server BDD")
    btn = gr.Button("Afficher utilisateurs")
    output = gr.Textbox(label="Liste des utilisateurs", interactive=False)
    btn.click(afficher_users, outputs=output)

if __name__ == "__main__":
    demo.launch(mcp_server=True)