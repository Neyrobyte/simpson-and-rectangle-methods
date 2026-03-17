import argparse as args
import math
import core

def args_parser():
    '''
    Парсер аргументов командной строки.
    '''
    parser = args.ArgumentParser(description='Математическое ядро для алгоритма вычисления площади криволинейной трапеции.')
    parser.add_argument('--method', '-m', type=str,   choices=['left', 'right', 'mid', 'simpson'], default='mid', help='Метод вычисления площади (left, right, mid, simpson)')
    parser.add_argument('--n',      '-n', type=int,   default=1000,    help='Количество разбиений интервала')
    parser.add_argument('--func',   '-f', type=str,   default='x**2',  help='Функция для интегрирования')
    parser.add_argument('--a',      '-a', type=float, default=0.0,     help='Начало интервала')
    parser.add_argument('--b',      '-b', type=float, default=1.0,     help='Конец интервала')
    return parser.parse_args()

def main():
    args = args_parser()
    print(f'\nВыбранный метод: {args.method}')
    print(f'Количество разбиений: {args.n}')
    print(f'Функция для интегрирования: {args.func}')
    print(f'Начало интервала: {args.a}')
    print(f'Конец интервала: {args.b}')

    # Вычисление значений функции на разбиении
    h = core.step_dividing(args.a, args.b, args.n)
    METHODS = {
        "left": rectangle_left,
        "right": rectangle_right,
        "mid": rectangle_mid,
        "simpson": simpson
    }
    method = METHODS[args.method]
    result = method(f, a, b, n)

    
    
main()