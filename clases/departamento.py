class Department():
    def __init__(self, id_department, name):
        self.id_department = id_department
        self.name = name
        self.Employee = []

    def add_employee(self, employee):
        self.employee.append(employee)
    
    def __str__(self):
        return f"Departamento: {self.name}, Empleados: {len(self.employee)}"