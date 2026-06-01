from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, paciente, profesional, especialidad, cita, horario
app = FastAPI()
origins = os.environ.get("CORS_ORIGINS", "*").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router)
app.include_router(paciente.router)
app.include_router(profesional.router)
app.include_router(especialidad.router)
app.include_router(cita.router)
app.include_router(horario.router)
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
