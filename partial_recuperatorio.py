nombres = []
cantidades = []
salir = True

while salir:
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")
    
    try:
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            nombres.append(nombre)
            cantidades.append(cantidad)
            print("Producto agregado con éxito")
        
        elif opcion == "2":
            print("Productos agotados:")
            agotados = False
            for i in range(len(nombres)):
                if cantidades[i] == 0:
                    print(nombres[i])
                    agotados = True
            if not agotados:
                print("No hay productos agotados")
        
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto: ")
            if not producto.strip():
                raise ValueError("El nombre no puede estar vacío")
            encontrado = False
            for i in range(len(nombres)):
                if nombres[i] == producto:
                    try:
                        nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                        if nueva_cantidad < 0:
                            raise ValueError("La cantidad no puede ser negativa")
                        cantidades[i] = nueva_cantidad
                        print("Stock actualizado")
                        encontrado = True
                        break
                    except ValueError as e:
                        print(f"Error: {str(e) if 'cantidad no puede ser negativa' in str(e) else 'Debe ingresar un número válido'}")
            if not encontrado:
                print("Producto no encontrado")
        
        elif opcion == "4":
            if not nombres:
                print("No hay productos registrados")
            else:
                print("\n=== Listado de productos ===")
                print(f"Total de productos: {len(nombres)}")
                print("-" * 30)
                for i in range(len(nombres)):
                    print(f"Producto: {nombres[i]} | Stock: {cantidades[i]}")
                print("-" * 30)
        
        elif opcion == "5":
            print("Gracias por usar el sistema")
            salir = False
        
        else:
            print("Opción inválida")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")