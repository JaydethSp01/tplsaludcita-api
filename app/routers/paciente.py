from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Paciente(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str

fake_pacientes_db = [
    Paciente(id=1, nombre="Juan Perez", email="juan@example.com", telefono="123456789"),
    Paciente(id=2, nombre="Maria Gomez", email="maria@example.com", telefono="987654321"),
]

@router.get("/pacientes", response_model=List[Paciente])
async def get_pacientes():
    return fake_pacientes_db

@router.post("/pacientes", response_model=Paciente)
async def create_paciente(paciente: Paciente):
    fake_pacientes_db.append(paciente)
    return paciente

@router.get("/pacientes/{paciente_id}", response_model=Paciente)
async def get_paciente(paciente_id: int):
    paciente = next((p for p in fake_pacientes_db if p.id == paciente_id), None)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return paciente

@router.put("/pacientes/{paciente_id}", response_model=Paciente)
async def update_paciente(paciente_id: int, paciente: Paciente):
    index = next((i for i, p in enumerate(fake_pacientes_db) if p.id == paciente_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    fake_pacientes_db[index] = paciente
    return paciente

@router.delete("/pacientes/{paciente_id}")
async def delete_paciente(paciente_id: int):
    index = next((i for i, p in enumerate(fake_pacientes_db) if p.id == paciente_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    del fake_pacientes_db[index]
    return {"message": "Paciente deleted"}
