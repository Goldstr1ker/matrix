def create_0_matrix(n: int, m: int) -> list:
    """Функция для создания матрицы n на m, заполненной нулями

    Args:
        n (int): число столбцов
        m (int): число колонок

    Returns:
        matrix: n lists with m zeros each all inside one list
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix
def print_matrix(matrix: list, space=3) -> None:
    """Печатает матрицу с отступом (3 default)

    Args:
        matrix (nested lists): матрица с произвольным размером
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(str(matrix[r][c]).ljust(space), end=' ')
        print()
def find_matrix_max(matrix: list) -> dict:
    """Находит максимальное число в матрице и его индекс

    Args:
        matrix (nested lists): матрица с произвольным размером

    Returns:
        dict: возвращает словарь, где ключ - максимальный элемент, а значение - список из двух его индексов
    """
    maximum = int(matrix[0][0])
    idx1=idx2=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if int(matrix[i][j])>maximum:
                maximum = int(matrix[i][j])
                idx1 = i
                idx2 = j
    max_element = {maximum: [idx1, idx2]}
    return max_element
def change_columns(matrix: list, change1: int, change2: int) -> list:
    """Взаимозаменят значения двух столбоцв в матрице

    Args:
        matrix (_type_): матрица размерама m на n
        change1 (int): индекс первого столбца для замены
        change2 (int): индекс второго столбца для замены

    Returns:
        matrix: новая матрица с заменёнными столбцами
    """
    for i in range(len(matrix)):
        matrix[i][change1], matrix[i][change2] = matrix[i][change2], matrix[i][change1]
    return matrix
def is_square(sqr_matrix: list)->bool:
    """Проверяет, квадратная ли матрица

    Args:
        sqr_matrix (list): матрица в виде вложенных списков

    Returns:
        bool: 
    """
    for row in sqr_matrix:
        if len(row) != len(sqr_matrix):
            return False
    else:
        return True
def is_simmetrical(sqr_matrix: list) -> bool:
    """Возвращает булевое значение, симметрична ли матрица

    Args:
        sqr_matrix (nested lists): квадратная матрица со стороной n

    Returns:
        bool: симметрична ли матрица
    """
    if is_square(sqr_matrix):
        pass
    else:
        return False
    flag = True
    for i in range(len(sqr_matrix)):
        for j in range(len(sqr_matrix)):
            if sqr_matrix[i][j]==sqr_matrix[j][i]:
                continue
            else:
                flag = False
                break
    return flag
def is_magic_square(matrix: list)->bool:
    """Возвращает, является ли матрица магическим квадратом. Матрица является им, если сумма значений по диагоналям, в каждом столбце истроке матрицы равны

    Args:
        matrix (list): квадратная матрица

    Returns:
        bool: 
    """
    flag = True
    
    checker_general = 0
    for element in matrix[0]:
            checker_general+=int(element)

    unique_list = [i for i in range(1, (len(matrix))**2+1)]
    matrix_unique = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
                matrix_unique.append(int(matrix[i][j]))
    for element in unique_list:
                if element in matrix_unique:
                    pass
                else:
                    flag = False
                    break
    for row in range(len(matrix)):
        row_int = [int(x) for x in matrix[row]]
        if sum(row_int)!= checker_general:
            flag = False
            break
        else:
            pass
        
    for column in range(len(matrix)):
        checker_columns = 0
        for numb in range(len(matrix)):
            checker_columns += int(matrix[numb][column])
        if checker_columns != checker_general:
            flag = False
            break
        else:
            pass

    checker_diagonals = 0
    checker_reverse_diagonals = 0
    for ind in range(len(matrix)):
        checker_diagonals += int(matrix[ind][ind])
        checker_reverse_diagonals += int(matrix[ind][len(matrix)-ind-1])
    if checker_diagonals != checker_reverse_diagonals:
        flag = False
    else:
        if checker_diagonals != checker_general:
            flag = False
        else:
            pass
    return flag
def create_012_matrix(n: int)->list:
    """Создаёт квадратную матрицу, где на побочной диагонали 1, ниже - двойки, выше - нули

    Args:
        n (int): сторона квадратной матрицы

    Returns:
        list: возвращает матрицу заполненную числами. Пример: [[0, 0, 1], [0, 1, 2], [1, 2, 2]]
    """
    matrix = create_0_matrix(n, n)

    for i in range(len(matrix)-1, 0, -1):
        for j in range(len(matrix)-1, len(matrix)-i-1, -1):
            matrix[i][j] = 2

    for i in range(n):
        matrix[i][len(matrix)-1-i] = 1
    return matrix
def create_sequence_matrix(n: int, m: int) -> list:
    """Создаёт матрицу n*m, последовательно заполненную числами от 1 до n*m

    Args:
        n (int): число строк(списков в составе матрицы)
        m (int): число строк(элементов в составе каждого из списков)

    Returns:
        list: матрица. Пример при n=2, m=3: [[1, 2, 3], [4, 5, 6]]
    """
    tracker = 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(tracker, tracker+m):
            row.append(j)
        matrix.append(row)
        tracker += m
    return matrix
def step_matrix(step: int, columns: int)-> list:
    """Функция для создания матрицы с шагом и числом строк step и числом колонок columns

    Args:
        step (int): шаг каждого элемента матрицы(начало с 1) и число колонок
        columns (int): число колонок в матрице

    Returns:
        list: матрица, в виде вложенных списков
    """
    matrix = []
    for i in range(1, step+1):
        row = []
        counter = 0
        for j in range(columns):
            num = i*counter
            row.append(num)
            counter+=1
        matrix.append(row)
    return matrix