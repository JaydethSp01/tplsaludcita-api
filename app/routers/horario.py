from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Horario(BaseModel):
    id: int
    profesional: str
    dia: str
    horaInicio: str
    horaFin: str

fake_horarios_db = [
    Horario(id=1, profesional="Dr. House", dia="Lunes", horaInicio="09:00", horaFin="12:00"),
    Horario(id=2, profesional="Dr. Smith", dia="Martes", horaInicio="10:00", horaFin="13:00"),
]

@router.get("/horarios", response_model=List[Horario])
async def get_horarios():
    return fake_horarios_db

@router.post("/horarios", response_model=Horario)
async def create_horario(horario: Horario):
    fake_horarios_db.append(horario)
    return horario

@router.get("/horarios/{horario_id}", response_model=Horario)
async def get_horario(horario_id: int):
    horario = next((h for h in fake_horarios_db if h.id == horario_id), None)
    if horario is None:
        raise HTTPException(status_code=404, detail="Horario not found")
    return horario

@router.put("/horarios/{horario_id}", response_model=Horario)
async def update_horario(horario_id: int, horario: Horario):
    index = next((i for i, h in enumerate(fake_horarios_db) if h.id == horario_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Horario not found")
    fake_horarios_db[index] = horario
    return horario

@router.delete("/horarios/{horario_id}")
async def delete_horario(horario_id: int):
    index = next((i for i, h in enumerate(fake_horarios_db) if h.id == horario_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Horario not found")
    del fake_horarios_db[index]
    return {"message": "Horario deleted"}
