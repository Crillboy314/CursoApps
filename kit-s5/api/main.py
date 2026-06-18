# ════════════════════════════════════════════════════════
# SESIÓN 5: API nivel 2 — parámetros + POST
#
# Correr:  uvicorn main:app --reload
# Docs:    http://127.0.0.1:8000/docs
# ════════════════════════════════════════════════════════

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── DATOS ────────────────────────────────────────────────
MIS_FRASES = [
    "Los datos no mienten, pero hay que saber preguntarles.",
    "Primero hazlo funcionar, luego hazlo bonito.",
    "El mejor código es el que se entiende en 6 meses.",
]

MIS_PELICULAS = [
    {"titulo": "Interstellar", "anio": 2014},
    {"titulo": "La La Land", "anio": 2016},
    {"titulo": "Whiplash", "anio": 2014},
]

# ══ BLOQUE 1: PARÁMETRO DE RUTA ══════════════════════════
# La variable va EN la URL: /frase/0, /frase/2
@app.get("/frase/{n}")
def una_frase(n: int):
    if 0 <= n < len(MIS_FRASES):
        return {"frase": MIS_FRASES[n]}
    return {"error": f"Solo tengo {len(MIS_FRASES)} frases (0 a {len(MIS_FRASES)-1})"}


# Combinando parámetro + lógica
@app.get("/saludo/{nombre}")
def saludo(nombre: str, idioma: str = "es"):
    # idioma es QUERY PARAM opcional: /saludo/Maria?idioma=en
    saludos = {"es": f"¡Hola {nombre}!", "en": f"Hello {nombre}!", "fr": f"Salut {nombre}!"}
    return {"mensaje": saludos.get(idioma, saludos["es"])}


# ══ BLOQUE 2: QUERY PARAMS ═══════════════════════════════
# La variable va DESPUÉS del ?: /peliculas?anio=2014
@app.get("/peliculas")
def peliculas(anio: int = None):
    if anio:
        filtradas = [p for p in MIS_PELICULAS if p["anio"] == anio]
        return {"peliculas": filtradas, "filtro": anio}
    return {"peliculas": MIS_PELICULAS}


# ══ BLOQUE 3: POST — recibir datos ═══════════════════════
# El "molde" de los datos que aceptamos
class Visita(BaseModel):
    nombre: str
    mensaje: str

# Lista en memoria (se borra al reiniciar — eso es intencional,
# da pie a hablar de bases de datos más adelante)
VISITAS = []

@app.post("/visitas")
def crear_visita(v: Visita):
    VISITAS.append(v)
    return {"ok": True, "total": len(VISITAS)}

@app.get("/visitas")
def listar_visitas():
    return {"visitas": VISITAS}
