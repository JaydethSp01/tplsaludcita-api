from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Cita(BaseModel):
    id: int
    paciente: str
    profesional: str
    fecha: str
    estado: str

fake_citas_db = [
    Cita(id=1, paciente="Juan Perez", profesional="Dr. House", fecha="2023-11-01", estado="Pendiente"),
    Cita(id=2, paciente="Maria Gomez", profesional="Dr. Smith", fecha="2023-11-02", estado="Confirmada"),
]

@router.get("/citas", response_model=List[Cita])
async def get_citas():
    return fake_citas_db

@router.post("/citas", response_model=Cita)
async def create_cita(cita: Cita):
    fake_citas_db.append(cita)
    return cita

@router.get("/citas/{cita_id}", response_model=Cita)
async def get_cita(cita_id: int):
    cita = next((c for c in fake_citas_db if c.id == cita_id), None)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita not found")
    return cita

@router.put("/citas/{cita_id}", response_model=Cita)
async def update_cita(cita_id: int, cita: Cita):
    index = next((i for i, c in enumerate(fake_citas_db) if c.id == cita_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Cita not found")
    fake_citas_db[index] = cita
    return cita

@router.delete("/citas/{cita_id}")
async def delete_cita(cita_id: int):
    index = next((i for i, c in enumerate(fake_citas_db) if c.id == cita_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Cita not found")
    del fake_citas_db[index]
    return {"message": "Cita deleted"}
