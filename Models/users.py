import uuid
from typing import Optional
from pydantic import BaseModel, Field

# Criando Schema No Banco
class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    nome: str = Field(...)
    idade: int = Field(...)
    github: str = Field(...)
    favLinguagens: str = Field(...)
    password: str = Field(...)
    email: str = Field(..., unique_items= None)

# Atualizando Schema
class UpdateUserSchema(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    idade: Optional[int]
    github: Optional[str]
    favLinguagens: Optional[str]
    password: Optional[str]
