from os import (getcwd as cwd)

from CronJob import (CronJob)

if __name__ == '__main__':
    job = CronJob()

    job.minute = 0
    job.hour = 0
    job.command = f'{cwd()}/update_pkgs.sh'

    job.register()

    # Segundo turno
    # Ej 1
    arr1 = [3, 2, 1]
    arr2 = [4, 5]
    arr3 = []

    i = 0
    while i < arr1.__len__():
        if arr1[i] == 1:
            arr3.append(arr1[i])
            arr1.pop(i)
        elif not arr1[i] % 2:
            arr2.append(arr1[i])
            arr1.pop(i)
        else:
            i += 1

    i = 0
    while i < arr2.__len__():
        if arr2[i] == 1:
            arr3.append(arr2[i])
            arr2.pop(i)
        elif arr2[i] % 2:
            arr1.append(arr2[i])
            arr2.pop(i)
        else:
            i += 1

    print(arr1, arr2, arr3, sep='\n')


    # Ej 2
    def bubble_sort(arr: list) -> [int]:
        i = 0
        while i < arr.__len__():
            min_value = min(arr[i:])
            if arr[i] > min_value:
                idx = arr.index(min_value)
                arr[i], arr[idx] = arr[idx], arr[i]

            i += 1

        return arr


    lista = input('Por favor introduzca la lista de números separados por coma:\n')
    lista = [int(n) for n in lista.split(sep=',')]

    lista = bubble_sort(lista)
    print(lista)
