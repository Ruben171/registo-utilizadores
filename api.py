from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
  return {"mensagem": "Olá, Ruben! A api está a funcionar"}

@app.get("/sobre")
def sobre():
  return {
      "nome": "Ruben",
      "idade": 26
  }

@app.get("/contacto")
def contacto():
  return {
      "email": "ruben@rmail.com",
      "telefone": "912345678"
  }

