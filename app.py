import gradio as gr
import sqlite3
import json

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

def get_db_schema_info():
    conn = None
    schema_info = {"tables": []}
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table_name_tuple in tables:
            table_name = table_name_tuple[0]
            table_data = {"name": table_name, "columns": []}

            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            for col_info in columns:
                table_data["columns"].append({
                    "name": col_info[1],
                    "type": col_info[2],
                    "primary_key": bool(col_info[5])
                })
            schema_info["tables"].append(table_data)
            
    finally:
        if conn:
            conn.close()
    
    return json.dumps(schema_info, indent=2)

with gr.Blocks() as demo:
    gr.Markdown("# MCP Server BDD")
    
    btn_display_users = gr.Button("Afficher utilisateurs")
    output_users = gr.Textbox(label="Liste des utilisateurs", interactive=False)
    btn_display_users.click(afficher_users, outputs=output_users)

    btn_display_schema = gr.Button("Afficher schéma BDD")
    output_schema = gr.Textbox(label="Schéma de la base de données", interactive=False)
    btn_display_schema.click(get_db_schema_info, outputs=output_schema)

if __name__ == "__main__":
    demo.launch(mcp_server=True)