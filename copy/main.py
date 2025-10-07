# Creamos una lista llamada 'lista' con tres nombres como elementos.
lista = ["alejandro", "pedro", "juan"]

# Usamos el método .copy() para crear una copia superficial (shallow copy) de la lista original.
# Esto significa que 'copiar_lista' será una nueva lista con los mismos valores,
# pero independiente de 'lista'. Si cambiamos un elemento en 'copiar_lista',
# la lista original no se verá afectada.
copiar_lista = lista.copy()

# Aquí cambiamos el primer elemento (índice 0) de 'copiar_lista' y le asignamos el valor "julian".
# Solo afecta a la copia, no a la lista original.
copiar_lista[0] = "julian"

# Imprimimos la lista original. 
# Como no la modificamos directamente, mantiene sus valores originales.
# Salida: ["alejandro", "pedro", "juan"]
print(lista)

# Imprimimos la lista copiada. 
# Como cambiamos su primer elemento, ahora tiene "julian" en lugar de "alejandro".
# Salida: ["julian", "pedro", "juan"]
print(copiar_lista)
