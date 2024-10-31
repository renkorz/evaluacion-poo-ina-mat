import sqlite3
from tabulate import tabulate

# Funciones para sub-menú de Empleados.
def add_employee(cnx):
    name = input("Nombre del empleado: ")
    position = input("Puesto: ")
    salary = float(input("Salario: "))
    id_department = int(input("ID de Departamento: "))
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO employee (name, position, salary, id_department) VALUES (?, ?, ?, ?)", (name, position, salary, id_department))
    cnx.commit()
    print (f"Empleado {name}, fue registrado correctamente.")

def view_employee(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM employee")
    employee = cursor.fetchall()
    headers = ["ID", "Nombre", "Puesto", "Salario", "ID Departamento"]
    print(tabulate(employee, headers=headers, tablefmt="pretty"))

def del_employee(cnx):
    id_employee = int(input("ID del Empleado a despedir: "))
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM employee WHERE id_employee = ?", (id_employee))
    cnx.commit()
    print(f"Se ha retirado como colaborador.")

# Funciones para sub-menú de departamentos.
def add_department(cnx):
    name = input("Nombre del Departamento: ")
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO department (name) VALUES (?)", (name,))
    cnx.commit()
    print("Departamento agregado correctamente.")

def view_deparment(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM department")
    employee = cursor.fetchall()
    headers = ["ID", "Nombre"]
    print(tabulate(employee, headers=headers, tablefmt="pretty"))

def del_department(cnx):
    id_department = int(input("ID del departmento a eliminar: "))
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM department WHERE id_department = ?", (id_department))
    cnx.commit()
    print("Departmaento eliminado.")


# Funciones para sub-menú de Proveedores
def add_supplier(cnx):
    name = input("Nombre del Proveedor: ")
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO supplier (name) VALUES (?)", (name,))
    cnx.commit()
    print("Proveedor agregado correctamente.")

def view_supplier(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM supplier")
    supplier = cursor.fetchall()
    headers = ["ID", "Nombre"]
    print(tabulate(supplier, headers=headers, tablefmt="pretty"))

def del_supplier(cnx):
    id_supplier = int(input("ID del Proveedor a eliminar: "))
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM supplier WHERE id_supplier = ?", (id_supplier))
    cnx.commit()
    print("Proveedor eliminado correctamente.")

# Funciones para sub-menú de 
def add_client(cnx):
    name = input("Nombre del cliente: ")
    contact = input("Contacto del cliente: ")
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO Cliente (nombre, contacto) VALUES (?, ?)", (name, contact))
    cnx.commit()
    print("Cliente agregado correctamente.")

def view_client(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client")
    client = cursor.fetchall()
    headers = ["ID", "Nombre", "Contacto"]
    print(tabulate(client, headers=headers, tablefmt="pretty"))

def del_client(cnx):
    id_client = input("ID del Cliente a eliminar: ")
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM client WHERE id_client = ?", (id_client))
    cnx.commit()
    print("Cliente fue eliminado correctamente.")

# Funciones para sub-menú de Facturas
def add_facture(cnx):
    id_client = int(input("ID del Cliente: "))
    total = float(input("Total factura: "))
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO facture (id_client, total) VALUES (?, ?)", (id_client, total))
    cnx.commit()
    print("Factura agregada correctamente.")

def view_facture(cnx):
    cursor = cnx.cursor
    cursor.execute("SELECT * FROM facture")
    facture = cursor.fetchall()
    headers = ("ID Factura", "ID Cliente", "TOTAL")
    print(tabulate(facture, headers=headers, tablefmt="pretty"))

def del_facture(cnx):
    id_facture = input("ID de la factura a eliminar: ")
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM facture WHERE id_facture = ?", (id_facture))
    cnx.commit()
    print("Factura eliminada correctamente.")
    
# Funciones para sub-menú de Producto
def add_product(cnx):
    name = input("Nombre del Producto: ")
    price = float(input("Precio: "))
    stock = int(input("Stock: "))
    id_inventory = int(input("ID del producto en inventario: "))
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO product (name, price, stock, id_inventory) VALUES (?, ?, ?, ?)", (name, price, stock, id_inventory))
    cnx.commit()
    print("Producto agregado correctamente.")