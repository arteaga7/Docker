# Docker


## ✨ Details


## 🌎 Structure

```
Simple-Agent/
├── main.py                 # Entrypoint, FastAPI app. Creates tables and seeds catalog on startup
├── app.py                  # Streamlit chat client
├── bot/
│   ├── config.py           # settings (lm model, api url, databse url, etc.)
│   ├── prompts.py          # promts
│   ├── api/                # routes (/chat, /health) + request schemas
│   ├── db/                 # SQLAlchemy engine, models, seed
│   ├── agent/              # llm client, conversation memory, tool-calling loop
│   └── tools/              # catalog / inventory / orders tools + registry
├── img/                    # Some pictures
├── Dockerfile
├── docker-compose.yml      # db (postgres) + api + ui
└── requirements.txt
└── .env                    # Contains API Key (not provided)
└── start.sh                # For deploying to Render.com
```

## ⚙️ Configuration
1. Clone this repository:
   ```bash
   git clone https://github.com/arteaga7/Docker.git
   ```
2. Create your .env file, with the following content:
   ```bash
   POSTGRES_DB=db_1
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=1234
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432  
   ```

## 🚀 Run with Docker
1. Clone and create .env file, as explained in 'Configuration' section.
2. Start everything (Postgres + Python + Jupyter):
   ```bash
   docker compose up --build
   ```
3. Open the UI at <http://localhost:8501>. 



## 🎯 Results
The chatbot is working correctly, responding politely to a greeting or a purchase order, as shwon in figs 1 and 2.
![alt text](<img/c1.png>)
Fig. 1.



