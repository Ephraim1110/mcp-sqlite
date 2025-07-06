# 🗄️ SQLite + LangChain + Ollama

## 🚀 Installation

```bash
pip install gradio langchain-community gradio-client
ollama pull qwen2.5
```

## 📁 Fichiers

- `app.py` - Serveur web Gradio + base SQLite
- `mcp_client.py` - Client IA avec LangChain  
- `test.db` - Base de données (créée automatiquement)

## 🎯 Utilisation

### 1. Lancer le serveur
```bash
python app.py
```
Interface web sur `http://localhost:7860`

### 2. Lancer l'agent IA
```bash
python mcp_client.py
```

### 3. Poser des questions
```
Pose ta question : Montre-moi les utilisateurs
Pose ta question : Quel est le schéma ?
Pose ta question : Combien y a-t-il d'utilisateurs ?
```

## 🗄️ Base de données

Table `users` avec 3 utilisateurs :
- alice (20 ans)
- bob (30 ans)  
- eve (40 ans)

## 🔧 Dépannage

- **Port occupé** : Changez le port dans `app.py`
- **Ollama manquant** : `ollama pull qwen2.5`
- **Erreur connexion** : Vérifiez que `app.py` est lancé

---

