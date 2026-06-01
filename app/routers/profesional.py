from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Profesional(BaseModel):
    id: int
    nombre: str
    especialidad: str
    email: str

fake_profesionales_db = [
    Profesional(id=1, nombre="Dr. House", especialidad="Diagnóstico", email="house@example.com"),
    Profesional(id=2, nombre="Dr. Smith", especialidad="Cardiología", email="smith@example.com"),
]

@router.get("/profesionales", response_model=List[Profesional])
async def get_profesionales():
    return fake_profesionales_db

@router.post("/profesionales", response_model=Profesional)
async def create_profesional(profesional: Profesional):
    fake_profesionales_db.append(profesional)
    return profesional

@router.get("/profesionales/{profesional_id}", response_model=Profesional)
async def get_profesional(profesional_id: int):
    profesional = next((p for p in fake_profesionales_db if p.id == profesional_id), None)
    if profesional is None:
        raise HTTPException(status_code=404, detail="Profesional not found")
    return profesional

@router.put("/profesionales/{profesional_id}", response_model=Profesional)
async def update_profesional(profesional_id: int, profesional: Profesional):
    index = next((i for i, p in enumerate(fake_profesionales_db) if p.id == profesional_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Profesional not found")
    fake_profesionales_db[index] = profesional
    return profesional

@router.delete("/profesionales/{profesional_id}")
async def delete_profesional(profesional_id: int):
    index = next((i for i, p in enumerate(fake_profesionales_db) if p.id == profesional_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Profesional not found")
    del fake_profesionales_db[index]
    return {"message": "Profesional deleted"}
