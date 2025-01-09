# Chatbotwpp

## Instale as dependencias utilizando: 
```bash
pip install -r requirements.txt
```


## Requisitos necessarios 
- Docker ou docker-compose
- Python versão 3.10 ou superior


## Inicie o banco vetorial

 Na pasta do arquivo execute
```bash
docker exec -it wpp_bot_api /bin/bash
```
Logo em seguida 
```bash
python app/rag/rag.py
```


## Para iniciar o bot, execute
```bash
docker-compose up --build
```

https://waha.devlike.pro