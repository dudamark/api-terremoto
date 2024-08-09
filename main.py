from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from banco import SessionLocal, init_db, Terremoto
from utilitarios import obter_dados_terremotos

app = FastAPI()

# Inicializar o banco de dados
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/salvar_terremotos/")
def salvar_terremotos(db: Session = Depends(get_db)):
    dados = obter_dados_terremotos()
    for item in dados:
        terremoto = Terremoto(
            magnitude=item["properties"]["mag"],
            latitude=item["geometry"]["coordinates"][1],
            longitude=item["geometry"]["coordinates"][0],
            localizacao=item["properties"]["place"]
        )
        db.add(terremoto)
    db.commit()
    return {"status": "Dados de terremotos salvos com sucesso!"}

@app.get("/terremotos/")
def listar_terremotos(db: Session = Depends(get_db)):
    terremotos = db.query(Terremoto).all()
    return terremotos
