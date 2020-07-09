from typing import Any, Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Material(BaseModel):
    name: str
    description: str


@app.get("/")
def fetch_root() -> Dict[str, str]:
    return {"Hello": "World"}


@app.get("/materials/{material_id}")
def fetch_material(material_id: int, q: Optional[str] = None) -> Dict[str, Any]:
    return {"material_id": material_id, "q": q}


@app.put("/materials/{material_id}")
def upload_material(material_id: int, material: Material) -> Dict[str, Any]:
    return {"material_id": material_id, "name": material.name, "description": material.description}
