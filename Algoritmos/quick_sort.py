"""
Quick Sort é recursivo (método que chama a si mesmo)
Algoritmo de dividir para conquistar
Muito eficiente para grandes conjuntos de dados

Pior caso é O(n^2)
Médio caso é O(n log n)
Perfomance depende em maior parte na seleção do pivot
"""

def quick_sort(lista):
   quick_sort_helper(lista,0,len(lista)-1)

def quick_sort_helper(lista,first,last):
   if first<last:
       splitpoint = partition(lista,first,last)
       quick_sort_helper(lista,first,splitpoint-1)
       quick_sort_helper(lista,splitpoint+1,last)

def partition(lista,first,last):
   pivotvalue = lista[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = lista[leftmark]
           lista[leftmark] = lista[rightmark]
           lista[rightmark] = temp

   temp = lista[first]
   lista[first] = lista[rightmark]
   lista[rightmark] = temp

   return rightmark

lista = [54,26,93,17,77,31,44,55,20]
quick_sort(lista)
print(lista)