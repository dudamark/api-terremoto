# api-terremoto
Criação de API com FastAPI para medição de terremotos mundiais

Iniciando o projeto consumindo do site https://earthquake.usgs.gov/fdsnws/event/1/query, para consumir informações de tremores de terra
ao redor do mundo. Os dados são salvos em uma base de dados SQLite e depois disponibilizados pelos endpoints.

Endpoint para recuperar os dados e salvar no banco: http://127.0.0.1:8000/salvar_terremotos/

Endpoint para exibir os dados da base de dados: http://127.0.0.1:8000/terremotos/

# Instruções de instalação

1 - Crie um ambiente virtual no dir do projeto: 

  python -m venv myvenv

2 - Ative o ambiente virtual:

  .\myvenv\Scripts\activate - Windows
  
  myvenv/bin/activate - Linux e MacOS

3 - Instale as bibliotecas do projeto:

  pip install -r requirements.txt

4 - Inicializar o servidor:

  uvicorn main:app --reload

Em breve novas atualizações como filtros e paginação.
