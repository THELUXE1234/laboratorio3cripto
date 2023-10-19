# Inicializa el contador de contraseñas
password_txt = 0
password_dic = 0

# Lee el archivo de entrada 'rockyou.txt' y crea un nuevo archivo 'rockyou_mod.dic'
with open('rockyou.txt', 'rb') as file, open('rockyou_mod.dic', 'w') as output_file:
    for line in file:
        # Decodifica la línea usando 'latin-1'
        decoded_line = line.decode('latin-1', errors='replace')
        # Elimina espacios en blanco al principio y al final de la línea
        line = decoded_line.strip()
        
        # Verifica si la línea no está vacía y comienza con una letra (ignora las que comienzan con números)
        if line:
            password_txt +=1
            if line[0].isalpha():
            
                # Convierte la primera letra en mayúscula y agrega '0' al final
                modified_line = line[0].upper() + line[1:] + '0\n'
                output_file.write(modified_line)
            
                # Incrementa el contador de contraseñas
                password_dic += 1

print("Proceso completado. Se ha creado 'rockyou_mod.dic'.")
print("Cantidad de contraseñas en 'rockyou.txt':", password_txt)
print("Cantidad de contraseñas en 'rockyou_mod.dic':", password_dic)

