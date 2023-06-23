#!/bin/python3

import math
import os
import random
import re
import sys

# Función para calcular la suma de los dígitos de un número
def digitSum(num):
    # Inicializamos la suma en 0
    sum = 0
    # Convertimos el número en una cadena de caracteres para poder iterar sobre sus dígitos
    num_str = str(num)
    # Iteramos sobre cada dígito y sumamos su valor numérico a la suma total
    for digit in num_str:
        sum += int(digit)
    # Retornamos la suma de los dígitos
    return sum

if __name__ == '__main__':
    # Leemos el valor de entrada
    n = int(input().strip())

    # Inicializamos las variables para el mejor divisor y la mayor suma de dígitos
    best_divisor = 1
    max_digit_sum = digitSum(n)

    # Iteramos desde 2 hasta la mitad del valor de entrada, buscando los divisores
    for i in range(2, n // 2 + 1):
        # Si el valor de entrada es divisible por el divisor actual
        if n % i == 0:
            # Calculamos la suma de los dígitos del divisor actual
            curr_digit_sum = digitSum(i)
            # Si la suma de los dígitos es mayor a la mayor suma encontrada hasta ahora,
            # actualizamos el mejor divisor y la mayor suma
            if curr_digit_sum > max_digit_sum:
                best_divisor = i
                max_digit_sum = curr_digit_sum
            # Si la suma de los dígitos es igual a la mayor suma encontrada hasta ahora,
            # comparamos los divisores y actualizamos el mejor divisor si es menor
            elif curr_digit_sum == max_digit_sum and i < best_divisor:
                best_divisor = i

    # Imprimimos el mejor divisor encontrado
    print(best_divisor)
