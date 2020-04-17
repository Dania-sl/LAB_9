import numpy as np
import random
import timeit


while True:
    while True:
        sort_method = input('What kind of sort you want use: selection, bubble, insertion, cocktail, Shell or heapsort: ')
        if sort_method == 'selection' or sort_method == 'bubble' or sort_method == 'insertion' or sort_method == 'cocktail' or sort_method == 'shell' or sort_method == 'heapsort':
            break
    if sort_method == 'selection':
        def selection_growth(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            for i in range(len_array - 1):
                min = i
                for j in range(i + 1, len_array):
                    count_of_comparisons += 1
                    if array[j] < array[min]:
                        min = j
                array[min], array[i] = array[i], array[min]
                count_of_permutations += 1
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")


        def selection_descending(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            for i in range(len_array - 1):
                min = i
                for j in range(i + 1, len_array):
                    count_of_comparisons += 1
                    if array[j] > array[min]:
                        min = j
                array[min], array[i] = array[i], array[min]
                count_of_permutations += 1
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")

    elif sort_method == 'bubble':
        def bubble_growth(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            i = 0
            flag = True
            while flag:
                flag = False
                for j in range(len_array - i - 1):
                    count_of_comparisons += 1
                    if array[j] > array[j + 1]:
                        array[j + 1], array[j] = array[j], array[j + 1]
                        count_of_permutations += 1
                        flag = True
                i += 1
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")


        def bubble_descending(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            i = 0
            flag = True
            while flag:
                flag = False
                for j in range(len_array - i - 1):
                    count_of_comparisons += 1
                    if array[j] < array[j + 1]:
                        array[j + 1], array[j] = array[j], array[j + 1]
                        count_of_permutations += 1
                        flag = True
                i += 1
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")

    elif sort_method == 'insertion':
        def insertion_growth(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            for i in range(1, len_array):
                j = i - 1
                key = array[i]
                while j >= 0 and array[j] > key:
                    count_of_comparisons += 2
                    array[j + 1] = array[j]
                    j -= 1
                    count_of_permutations += 1
                array[j + 1] = key
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")


        def insertion_descending(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            len_array = len(array)
            for i in range(1, len_array):
                j = i - 1
                key = array[i]
                while j >= 0 and array[j] < key:
                    count_of_comparisons += 2
                    array[j + 1] = array[j]
                    j -= 1
                    count_of_permutations += 1
                array[j + 1] = key
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")
    elif sort_method == 'cocktail':
        def cocktail_growth(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            for i in range(len(array) // 2):
                swap = False
                for j in range(1 + i, len(array) - i):
                    if array[j] < array[j - 1]:
                        count_of_comparisons += 1
                        array[j], array[j - 1] = array[j - 1], array[j]
                        count_of_permutations += 1
                        swap = True
                if not swap:
                    break
                swap = False
                for j in range(len(array) - i - 1, i, -1):
                    if array[j] < array[j - 1]:
                        count_of_comparisons += 1
                        array[j], array[j - 1] = array[j - 1], array[j]
                        count_of_permutations += 1
                        swap = True
                if not swap:
                    break
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")


        def cocktail_descending(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            for i in range(len(array) // 2):
                swap = False
                for j in range(1 + i, len(array) - i):
                    if array[j] > array[j - 1]:
                        count_of_comparisons += 1
                        array[j], array[j - 1] = array[j - 1], array[j]
                        count_of_permutations += 1
                        swap = True
                if not swap:
                    break
                swap = False
                for j in range(len(array) - i - 1, i, -1):
                    if array[j] > array[j - 1]:
                        count_of_comparisons += 1
                        array[j], array[j - 1] = array[j - 1], array[j]
                        count_of_permutations += 1
                        swap = True
                if not swap:
                    break
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")

    elif sort_method == 'shell':
        def shell_growth(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            mid = len(array) // 2
            while mid:
                for i, j in enumerate(array):
                    while i >= mid and array[i - mid] > j:
                        count_of_comparisons += 2
                        array[i] = array[i - mid]
                        count_of_permutations += 1
                        i -= mid
                    array[i] = j
                mid = 1 if mid == 2 else int(mid * 5.0 / 11)
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")


        def shell_descending(array):
            count_of_permutations = 0
            count_of_comparisons = 0
            mid = len(array) // 2
            while mid:
                for i, j in enumerate(array):
                    while i >= mid and array[i - mid] < j:
                        count_of_comparisons += 2
                        array[i] = array[i - mid]
                        count_of_permutations += 1
                        i -= mid
                    array[i] = j
                mid = 1 if mid == 2 else int(mid * 5.0 / 11)
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")

    elif sort_method == 'heapsort':
        def heapify(array, n, i, count_of_comparisons, count_of_permutations):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            count_of_permutations += 1
            if l < n and array[i] < array[l]:
                largest = l
            count_of_permutations += 1
            if r < n and array[largest] < array[r]:
                largest = r
            if largest != i:
                count_of_comparisons += 1
                array[i], array[largest] = array[largest], array[i]
                count_of_permutations, count_of_comparisons = heapify(array, n, largest, count_of_comparisons, count_of_permutations)
            return count_of_comparisons, count_of_permutations

        def heapSort_growth(array):
            count_of_comparisons = 0
            count_of_permutations= 0
            n = len(array)
            heapify(array, n, 0, count_of_comparisons, count_of_permutations)
            for i in range(n, -1, -1):
                count_of_permutations, count_of_comparisons = heapify(array, n, i, count_of_comparisons, count_of_permutations)
            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                count_of_comparisons += 1
                heapify(array, i, 0, count_of_comparisons, count_of_permutations)
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")

        def heapify_2(array, n, i, count_of_comparisons, count_of_permutations):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            count_of_permutations += 1
            if l < n and array[i] > array[l]:
                largest = l
            count_of_permutations += 1
            if r < n and array[largest] > array[r]:
                largest = r
            if largest != i:
                count_of_comparisons += 1
                array[i], array[largest] = array[largest], array[i]
                count_of_permutations, count_of_comparisons = heapify_2(array, n, largest, count_of_comparisons, count_of_permutations)
            return count_of_comparisons, count_of_permutations

        def heapSort_descending(array):
            count_of_comparisons = 0
            count_of_permutations= 0
            n = len(array)
            heapify_2(array, n, 0, count_of_comparisons, count_of_permutations)
            for i in range(n, -1, -1):
                count_of_permutations, count_of_comparisons = heapify_2(array, n, i, count_of_comparisons, count_of_permutations)
            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                count_of_comparisons += 1
                heapify_2(array, i, 0, count_of_comparisons, count_of_permutations)
            print(array)
            print(count_of_comparisons)
            print(count_of_permutations)
            t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
            print(f"Program was executed by {t} seconds")
    else:
        break
    while True:
        type_entering = input('Specify which type of list you want to use: random or own: ')
        if type_entering == 'random' or type_entering == 'own':
            break
    if type_entering == 'random':
        main_array = np.random.randint(1, 50, 100)
    else:
        while True:
            try:
                main_array = np.zeros(10, dtype=int)
                for i in range(len(main_array)):
                    main_array[i] = int(input('Enter element: '))
                break
            except ValueError:
                print('Enter correct value')

    n = len(main_array)
    if sort_method == 'bubble':
        bubble_descending(main_array)
        bubble_growth(main_array)
    elif sort_method == 'selection':
        selection_growth(main_array)
        selection_descending(main_array)
    elif sort_method == 'insertion':
        insertion_growth(main_array)
        insertion_descending(main_array)
    elif sort_method == 'cocktail':
        cocktail_growth(main_array)
        cocktail_descending(main_array)
    elif sort_method == 'shell':
        shell_growth(main_array)
        shell_descending(main_array)
    elif sort_method == 'heapsort':
        heapSort_growth(main_array)
        heapSort_descending(main_array)
    if input() != '':
        break
    print()

