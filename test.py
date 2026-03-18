import file_manager

while True:
    print("-- Que quieres hacer? --")
    print("1. Crear Carpeta.")
    print("2. Crear Archivo.")
    print("3. Ver Contenido de la carpeta/archivo")
    print("4. Renombrar archivo o carpeta.")
    print("5, Borrar carpeta o archivo.")
    print("6. Salir.")

    cuestion = input("Eligir opcion: ")

    if cuestion == "1":
        name = input("Escribe nombre: ")
        result = file_manager.create_folder(name)
        print(f"{result}")
        continue

    elif cuestion == "2":
        name = input("Escribe nombre: ")
        result = file_manager.create_file(name)
        print(f"{result}")
        continue

    elif cuestion =="3":
        name = input("Escribe el nombre de la carpeta/archivo para ver su contenido: ")
        result = file_manager.list_files(name)

    elif cuestion == "4":
        old_name = input("Escribe el nombre actual del archivo/carpeta: ")
        new_name = input("Escribe el nuevo nombre: ")

        result = file_manager.rename(old_name, new_name)
        print(f"{result}")
        continue

    elif cuestion == "5":
        try:
            name = input("Escribe el nombre del archivo o carpeta a borrar: ")

            result = file_manager.delete(name)
            print(f"{result}")
            continue
        except FileNotFoundError:
            print(f"Error el archivo {name} no existe.")

    elif cuestion == "6":
        print("Gracias por usar este gestor de archivos!")
        break
    else:
        print("Error: opcion no valida intentalo otra vez.")
        continue
