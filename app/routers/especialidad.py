from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Especialidad(BaseModel):
    id: int
    nombre: str

fake_especialidades_db = [
    Especialidad(id=1, nombre="Cardiología"),
    Especialidad(id=2, nombre="Dermatología"),
]

@router.get("/especialidades", response_model=List[Especialidad])
async def get_especialidades():
    return fake_especialidades_db

@router.post("/especialidades", response_model=Especialidad)
async def create_especialidad(especialidad: Especialidad):
    fake_especialidades_db.append(especialidad)
    return especialidad

@router.get("/especialidades/{especialidad_id}", response_model=Especialidad)
async def get_especialidad(especialidad_id: int):
    especialidad = next((e for e in fake_especialidades_db if e.id == especialidad_id), None)
    if especialidad is None:
        raise HTTPException(status_code=404, detail="Especialidad not found")
    return especialidad

@router.put("/especialidades/{especialidad_id}", response_model=Especialidad)
async def update_especialidad(especialidad_id: int, especialidad: Especialidad):
    index = next((i for i, e in enumerate(fake_especialidades_db) if e.id == especialidad_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Especialidad not found")
    fake_especialidades_db[index] = especialidad
    return especialidad

@router.delete("/especialidades/{especialidad_id}")
async def delete_especialidad(especialidad_id: int):
    index = next((i for i, e in enumerate(fake_especialidades_db) if e.id == especialidad_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Especialidad not found")
    del fake_especialidades_db[index]
    return {"message": "Especialidad deleted"}
