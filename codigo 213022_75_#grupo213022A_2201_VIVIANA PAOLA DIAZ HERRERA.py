# Matriz de inventario
matriz_inventario = [["Código", "Nombre", "Stock Actual", "Stock Mínimo"]]
inventario = [
    [101, "Laptop", 5, 10],
    [102, "Mouse", 20, 15],
    [103, "Teclado", 8, 12],
    [104, "Monitor", 2, 5],
    [105, "Cable HDMI", 30, 20]
]  # Coma al final de la lista

# Módulo (función) para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Proceso principal
print("--- Informe de Auditoría de Inventario ---")
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    actual = articulo[2]
    minimo = articulo[3]
    
    cantidad_a_pedir = calcular_pedido(actual, minimo)
    
    print(f"Artículo: {nombre} | Cantidad a solicitar: {cantidad_a_pedir}")
    
    