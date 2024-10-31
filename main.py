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

# Funciones para sub-menú de Clientes
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
    headers = ["ID Factura", "ID Cliente", "TOTAL"]
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

def view_product(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM product")
    product = cursor.fetchall()
    headers = ["ID Producot", "Nombre", "Precio", "Stock", "ID Inventario"]
    print(tabulate(product, headers=headers, tablefmt="pretty"))

def del_product(cnx):
    id_product = input("ID de producto a eliminar: ")
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM product WHERE id_product = ?", (id_product))
    cnx.commit()
    print("Producto eliminado correctamente.")

# Funciones para sub-menú de Proyecto.
def add_project(cnx):
    name = input("Nombre del proyecto: ")
    budget = float(input("Presupuesto: "))
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO project (name, budget) VALUES (?, ?)", (name, budget))
    cnx.commit()
    print("Proyecto agregado correctamente")

def view_project(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM project")
    project = cursor.fetchall()
    headers = ["ID Proyecto", "Nombre", "Presupuesto"]
    print(tabulate(project, headers=headers, tablefmt="pretty"))

def del_project(cnx):
    id_project = input("ID de proyecto a eliminar: ")
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM project WHERE id_project = ?", (id_project))
    cnx.commit()
    print("Proyecto eliminado correctamente.")


# Sub-menú por área.
def menu_employee(cnx):
    while True:
        print("\n--- Menú de Empleados ---")
        print("1. Agregar empleado.")
        print("2. Ver empleados.")
        print("3. Eliminar empleado.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_employee(cnx)
        elif option == "2":
            view_employee(cnx)
        elif option == "3":
            del_employee(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

def menu_department(cnx):
    while True:
        print("\n--- Menú de Departamentos ---")
        print("1. Agregar departamento.")
        print("2. Ver departamentos.")
        print("3. Eliminar departamento.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_department(cnx)
        elif option == "2":
            view_deparment(cnx)
        elif option == "3":
            del_department(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

def menu_supplier(cnx):
    while True:
        print("\n--- Menú de Proveedores ---")
        print("1. Agregar proveedor.")
        print("2. Ver proveedores.")
        print("3. Eliminar proveedor.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_supplier(cnx)
        elif option == "2":
            view_supplier(cnx)
        elif option == "3":
            del_supplier(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

def menu_client(cnx):
    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Agregar cliente.")
        print("2. Ver clientes.")
        print("3. Eliminar cliente.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_client(cnx)
        elif option == "2":
            view_client(cnx)
        elif option == "3":
            del_client(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

def menu_facture(cnx):
    while True:
        print("\n--- Menú de Facturas ---")
        print("1. Agregar factura.")
        print("2. Ver facturas.")
        print("3. Eliminar factura.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_facture(cnx)
        elif option == "2":
            view_facture(cnx)
        elif option == "3":
            del_facture(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

def menu_product(cnx):
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Agregar producto.")
        print("2. Ver productos.")
        print("3. Eliminar producto.")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            add_product(cnx)
        elif option == "2":
            view_product(cnx)
        elif option == "3":
            del_product(cnx)
        elif option == "4":
            return
        else:
            print("Opción no válida.")

# Menu general
def menu_general(cnx):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Menú de Empleados")
        print("2. Menú de Departamentos")
        print("3. Menú de Proveedores")
        print("4. Menú de Clientes")
        print("5. Menú de Facturas")
        print("6. Menú de Productos")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            menu_employee(cnx)
        elif opcion == "2":
            menu_department(cnx)
        elif opcion == "3":
            menu_supplier(cnx)
        elif opcion == "4":
            menu_client(cnx)
        elif opcion == "5":
            menu_facture(cnx)
        elif opcion == "6":
            menu_product(cnx)
        elif opcion == "7":
            print("Saliendo del programa. Guardando datos.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función principal

def main():
    cnx = sqlite3.connect('empresa.db')
    try:
        menu_general(cnx)
    finally:
        cnx.close()
        
if __name__ == "__main__":
    main()
