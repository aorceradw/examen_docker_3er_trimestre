def calcular_precio_final(precio,descuento):
    """
    PEP 257 ejercicio 7 
    """
   
   try:
    for item in precio:
        print("El precio final con descuento es", precio/descuento)