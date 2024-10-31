class Project():
    def __init__(self, id_project, name, budget, employee=[]):
        self.id_project = id_project
        self.name = name
        self.budget = budget
        self.employee = employee

    def assign_employee(self, employee):
        self.employee.append(employee)

    def __str__(self):
        return f"Proyecto: {self.name}, Presupuesto: {self.budget}"