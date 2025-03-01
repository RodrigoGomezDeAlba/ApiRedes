from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_raiz():
    return "Primer get automatico"

@app.get("/Bienvenida/{nombre}")
def saludar(nombre: str):
    return {f"Hola, {nombre}, como estas?"}

@app.get("/Despedida/{lugar}")
def despedida(lugar: str):
    return {f"Adios, nos vemos en {lugar}."}

@app.post("/crear_usuario/")
def crear_usuario(nombre: str, edad: int):
    return {"nombre": nombre, "edad": edad, "mensaje": "Usuario creado exitosamente"}