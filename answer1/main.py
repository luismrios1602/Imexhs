def hanoi(n, origen, destino, auxiliar):
    global rods

    if n == 1:
        # Tomar el disco superior de origen
        disco = rods[origen].pop()
        # Colocar en destino
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
    (1, "blue")
]

rods = [disks.copy(), [], []]

hanoi(len(disks), 0, 2, 1)

print("\nEstado final de las torres:")
for i, torre in enumerate(rods):
    print(f"Torre {i}: {torre}")
