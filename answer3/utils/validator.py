from typing import List

def isNumber(data: List[str]):
    for row in data:
        info_data = row.split(' ')
        for char in info_data:
            try:
                numero = int(char)
                print("Es un string que representa un entero:", numero)
            except ValueError:
                print("No es un entero válido")
                return False
            
    return True