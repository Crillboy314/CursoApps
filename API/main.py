from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random 

# 1. Crear la app — una línea y tu API ya existe
app = FastAPI()

# 2. CORS: permite que tu HTML (que es "otro origen")
#    pueda llamar a esta API. SIN ESTO el navegador bloquea
#    la petición y sale un error rojo en la consola.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── TUS DATOS (los estudiantes ponen los suyos) ──────────
MI_NOMBRE = "Kevin Rojas"
MI_CIUDAD = "Quito"
MI_PROFESION = "Matemático y docente de Ciencia de Datos"

MIS_FRASES = [
    "Los datos no mienten, pero hay que saber preguntarles.",
    "Primero hazlo funcionar, luego hazlo bonito.",
    "El mejor código es el que se entiende en 6 meses.",
    "Esta es la frase número 4 de código.",
    "Esta es la frase número 5 de datos.",
]

MIS_PELICULAS = [
    {"titulo": "Interstellar", "anio": 2014},
    {"titulo": "La La Land", "anio": 2016},
    {"titulo": "El secreto de sus ojos", "anio": 2009},
]

MIS_COMIDAS = [
    {"nombre": "Ceviche", "tipo": "Plato principal"},
    {"nombre": "Lomo saltado", "tipo": "Plato principal"},
    {"nombre": "Tiramisu", "tipo": "Postre"},
]
# ── ENDPOINTS ────────────────────────────────────────────

# El más simple posible: GET /hola
@app.get("/hola")
def saludo():
    return {"mensaje": "Hola mundo desde mi propia API 🐍"}

# GET /sobre-mi — devuelve un objeto JSON
@app.get("/sobre-mi")
def sobre_mi():
    return {
        "nombre": MI_NOMBRE,
        "ciudad": MI_CIUDAD,
        "profesion": MI_PROFESION,
    }

# GET /peliculas — devuelve la lista de películas
@app.get("/peliculas")
def get_peliculas():
    return {"peliculas": MIS_PELICULAS}

# GET /frase-aleatoria — devuelve una frase al azar
@app.get("/frase-aleatoria")
def frase_aleatoria():
    return {"frase": random.choice(MIS_FRASES)}
    
@app.get("/comidas")
def get_comidas():
    return {"comidas": MIS_COMIDAS}

@app.get("/frase/{frase_id}")
def obtener_frase_por_id(frase_id: int):
    # Validamos que el ID exista en la lista para que la app no se caiga
    if frase_id < 0 or frase_id >= len(MIS_FRASES):
        return {"error": f"Frase no encontrada. Usa un ID entre 0 y {len(MIS_FRASES) - 1}"}
    
    return {
        "id": frase_id,
        "frase": MIS_FRASES[frase_id]
    }
    
# GET /buscar-frase?keyword=datos
@app.get("/buscar-frase")
def buscar_frase(keyword: str):
    # Filtramos la lista: convertimos todo a minúsculas para que no importe si escriben con mayúsculas
    resultados = [frase for frase in MIS_FRASES if keyword.lower() in frase.lower()]
    
    return {
        "busqueda": keyword,
        "resultados_encontrados": len(resultados),
        "frases": resultados
    }
    
# ...existing code...

# GET /pelicula/{pelicula_id} — devuelve una película por ID
@app.get("/pelicula/{pelicula_id}")
def obtener_pelicula_por_id(pelicula_id: int):
    if pelicula_id < 0 or pelicula_id >= len(MIS_PELICULAS):
        return {"error": f"Película no encontrada. Usa un ID entre 0 y {len(MIS_PELICULAS) - 1}"}
    
    return {
        "id": pelicula_id,
        "pelicula": MIS_PELICULAS[pelicula_id]
    }

# GET /buscar-pelicula?keyword=Interstellar
@app.get("/buscar-pelicula")
def buscar_pelicula(keyword: str):
    resultados = [pelicula for pelicula in MIS_PELICULAS if keyword.lower() in pelicula["titulo"].lower()]
    
    return {
        "busqueda": keyword,
        "resultados_encontrados": len(resultados),
        "peliculas": resultados
    }

# ...existing code...

# GET /buscar-pelicula?keyword=Interstellar
@app.get("/buscar-pelicula")
def buscar_pelicula(keyword: str):
    resultados = [pelicula for pelicula in MIS_PELICULAS if keyword.lower() in pelicula["titulo"].lower()]
    
    return {
        "busqueda": keyword,
        "resultados_encontrados": len(resultados),
        "peliculas": resultados
    }

# GET /peliculas-aleatorias — devuelve 2 películas al azar
@app.get("/peliculas-aleatorias")
def peliculas_aleatorias():
    peliculas_random = random.sample(MIS_PELICULAS, 2)
    return {
        "peliculas": peliculas_random
    }

# ── ENDPOINTS TIPO POST (Para modificar datos) ──────────

# POST /modificar-nombre?nuevo_nombre=Kevin+Rojas+Pro
@app.post("/modificar-nombre")
def modificar_nombre(nuevo_nombre: str):
    global MI_NOMBRE  # Indicamos a Python que modificaremos la variable global
    MI_NOMBRE = nuevo_nombre
    
    return {
        "mensaje": "Nombre actualizado con éxito",
        "nombre_actual": MI_NOMBRE
    }


# POST /agregar-frase?nueva_frase=El+conocimiento+es+poder
@app.post("/agregar-frase")
def agregar_frase(nueva_frase: str):
    global MIS_FRASES  # Accedemos a la lista global
    MIS_FRASES.append(nueva_frase)  # Añadimos la frase al final de la lista
    
    return {
        "mensaje": "Frase añadida con éxito",
        "id_asignado": len(MIS_FRASES) - 1,
        "frase_añadida": nueva_frase,
        "total_frases": len(MIS_FRASES)
    }


# POST /agregar-pelicula?titulo=Inception&anio=2010
@app.post("/agregar-pelicula")
def agregar_pelicula(titulo: str, anio: int):
    global MIS_PELICULAS  # Accedemos a la lista de diccionarios
    
    # Creamos la estructura del diccionario para la nueva película
    nueva_pelicula = {"titulo": titulo, "anio": anio}
    MIS_PELICULAS.append(nueva_pelicula)
    
    return {
        "mensaje": "Película añadida con éxito",
        "id_asignado": len(MIS_PELICULAS) - 1,
        "pelicula_añadida": nueva_pelicula,
        "total_peliculas": len(MIS_PELICULAS)
    }