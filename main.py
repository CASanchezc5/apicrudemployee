from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List

# Definimos el modelo de datos
class Employee(BaseModel):
    id: int 
    name: str 
    age: int 
    email: str 
    phone: str 
    salary: float

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Lista en memoria para almacenar los "items" (diccionarios)
employees_db = []
@app.get("/")
async def home():
    return {"message":"Estamos en inicio"}
# CRUD - Crear un empleado
@app.post("/employees/", response_model=Employee)
async def create_employee(employee: Employee):
    # Añadimos el item a la lista
    employees_db.append(employee)
    return employee

# CRUD - Leer todos los items
@app.get("/employees/", response_model=List[Employee])
async def get_employees():
    return employees_db

# CRUD - Leer un item por ID
@app.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    for employee in employees_db:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Empleado no enncotrado")

# CRUD - Actualizar un item por ID
@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Empleado no enncotrado")

# CRUD - Eliminar un item por ID
@app.delete("/employees/{employee_id}", response_model=Employee)
async def delete_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            deleted_employee = employees_db.pop(index)
            return deleted_employee
    raise HTTPException(status_code=404, detail="Empleado no enncotrado")