steps = 0

def hanoi(n, origen, destino, auxiliar):
    global rods, steps

    # print(f'n: {n}')
    
    if n == 1:
        steps += 1

        # Tomar el disco superior de origen
        disco = rods[origen].pop()
        # Colocar en destino

        if len(rods[destino]) > 0:
            print(f'disco: {disco} - Ultimo Destino: {rods[destino][-1]}')

            #We validate the same color for the last disk in the destiny rod
            if disco[1] == rods[destino][-1][1]: 
                #If it's the same, so we must raise a exception
                raise ValueError('Impossible to complete the transfer')
        
        rods[destino].append(disco)
        print(f"Mover disco {disco} de torre {origen} a torre {destino}")
    else:
        # Mover n-1 discos al auxiliar
        hanoi(n - 1, origen, auxiliar, destino)
        # Mover el disco más grande al destino
        hanoi(1, origen, destino, auxiliar)
        # Mover los n-1 discos sobre el grande
        hanoi(n - 1, auxiliar, destino, origen)

# Inicialización
disks = [
    (5, "red"),
    (4, "blue"),
    (3, "red"),
    (2, "green"),
    (1, "red")
]

rods = [disks.copy(), [], []]

try:
    hanoi(len(disks), 0, 2, 1)
except ValueError as ex:
    print(ex)

print("\nEstado final de las torres:")
for i, torre in enumerate(rods):
    print(f"Torre {i}: {torre}")

print(f'Pasos: {steps}')
