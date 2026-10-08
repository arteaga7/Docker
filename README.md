# Docker


## ✨ Details
PostgreSQL iniciará primero, validará que esté listo y ejecutará el script init.sql.

Python App arrancará automáticamente después, se conectará a la base de datos e imprimirá los registros en tu consola.

Jupyter Notebook iniciará en segundo plano. Podrás acceder a él abriendo en tu navegador el enlace que aparece en la terminal (incluye un token de seguridad generado por Jupyter, por ejemplo: [http://127.0.0.1:8888/?token=](http://127.0.0.1:8888/?token=)...).

## 🌎 Structure
```
Docker/
└── jupyter/
    └── Dockerfile
    └── notebook.ipynb
├── postgres/
    └── init.sql
├── python/
    └── Dockerfile
    └── requirements.txt
    └── app.py
└── .env                    # Contains postgres settings (not provided)
└── compose.yml
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
2. Start everything (Postgres + Python + Jupyter) with the following command (first time only):
   ```bash
   docker compose up --build
   ```
3. Open the UI at <http://localhost:8501>. 
4. Close everything with:
   ```bash
   docker compose down
   ```

   If Docker is not running, use (linux):
   ```bash
   sudo systemctl start docker
   ```


## 🎯 Results
The chatbot is working correctly, responding politely to a greeting or a purchase order, as shwon in figs 1 and 2.
![alt text](<img/c1.png>)
Fig. 1.



