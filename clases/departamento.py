class Departamento():
    def __init__(self, id_departament, name):
        self.id_departament = id_departament
        self.name = name
        self.Employee = []

    def agregar_empleados(self, employee):
        self.employee.append(employee)
    
    def __str__(self):
        return f"Departamento: {self.name}, Empleados: {len(self.employee)}"