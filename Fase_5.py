def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Devuelve la cantidad exacta a pedir para un artículo.

    Si el stock actual es menor al mínimo, se pide la diferencia.
    Si el stock actual es suficiente, retorna 0.
    """
    return max(stock_minimo - stock_actual, 0)


def cargar_inventario():
    """Crea la matriz de inventario con al menos 5 artículos."""
    return [
        [101, "Lapiceros", 15, 20],
        [102, "Cuadernos", 12, 10],
        [103, "Borradores", 3, 8],
        [104, "Carpetas", 25, 25],
        [105, "Marcadores", 7, 15],
        [106, "Resaltadores", 4, 10],
    ]


def generar_lista_pedidos(inventario):
    """Genera una lista de artículos que necesitan reabastecimiento."""
    pedidos = []
    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        pedidos.append([codigo, nombre, stock_actual, stock_minimo, cantidad])
    return pedidos


def imprimir_reporte_pedidos(pedidos):
    """Imprime el reporte de pedidos con formato claro y profesional."""
    articulos_a_pedir = [p for p in pedidos if p[4] > 0]
    print("\n=== Auditoría de Inventario ===")
    print(f"Total de artículos evaluados: {len(pedidos)}")
    print(f"Artículos con reabastecimiento necesario: {len(articulos_a_pedir)}")

    if not articulos_a_pedir:
        print("Todos los artículos tienen stock suficiente. No se requiere pedido.")
        return

    print("\nLista de pedidos:")
    print(f"{'Código':<8} {'Artículo':<15} {'Stock':>7} {'Mínimo':>9} {'A pedir':>9}")
    print('-' * 52)
    total_unidades = 0
    for codigo, nombre, stock_actual, stock_minimo, cantidad in articulos_a_pedir:
        total_unidades += cantidad
        print(f"{codigo:<8} {nombre:<15} {stock_actual:>7} {stock_minimo:>9} {cantidad:>9}")

    print('-' * 52)
    print(f"Total unidades a pedir: {total_unidades}")


def imprimir_inventario(inventario):
    """Imprime el inventario completo y su estado actual."""
    print("Inventario actual:")
    print(f"{'Código':<8} {'Artículo':<15} {'Stock':>7} {'Mínimo':>9}")
    print('-' * 42)
    for codigo, nombre, stock_actual, stock_minimo in inventario:
        estado = "OK" if stock_actual >= stock_minimo else "BAJO"
        print(f"{codigo:<8} {nombre:<15} {stock_actual:>7} {stock_minimo:>9}   {estado}")


def main():
    inventario = cargar_inventario()
    imprimir_inventario(inventario)

    pedidos = generar_lista_pedidos(inventario)
    imprimir_reporte_pedidos(pedidos)


if __name__ == "__main__":
    main()
