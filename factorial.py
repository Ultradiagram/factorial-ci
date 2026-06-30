def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
        numero (int): Número entero mayor o igual a 0.

    Retorna:
        int: El factorial del número.

    Excepciones:
        TypeError: Si el valor no es un número entero.
        ValueError: Si el número es negativo.
    """
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero")

    if numero < 0:
        raise ValueError("El número no puede ser negativo")

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado