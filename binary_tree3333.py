#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd
from time import perf_counter
from random import randint, sample


# In[2]:


class BST:
    def __init__(self,key): 
        self.key = key 
        self.lchild = None
        self.rchild = None
        

    def insert(self,data):
        ''' функция для вставки данных в дерево '''
        if self.key is None:
            self.key = data
            return True
        if self.key == data:
            return False #Дерево не может содержать повторяющихся данных
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
                return True
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                return True

    def insert_any(self, data):
        ''' функция для вставки данных в дерево с повторяющимися элементами'''
        if self.key:
            if data <= self.key:
                if self.lchild is None:
                    self.lchild = BST(data)
                else:
                    self.lchild.insert_any(data)
            elif data > self.key:
                if self.rchild is None:
                    self.rchild = BST(data)
                else:
                    self.rchild.insert_any(data)
        else:
            self.key = data
    
    def search(self, data):
        ''' Эта функция проверяет, находятся ли указанные данные в дереве или нет. 
        возвращает true если найдет и false в противном случае '''
        if(data == self.key):
            return True
        elif(data < self.key):
            if self.lchild:
                return self.lchild.search(data)
            else:
                return False
        else:
            if self.rchild:
                return self.rchild.search(data)
            else:
                return False
                
    def delete(self, data):
        curr = self.key
        if self.lchild == None and self.rchild == None and data == curr:
            self.key = None
            return self
        else:
            return self.delete2(data,curr)
    
    def delete2(self,data,curr):
        ''' функция для удаления ключа '''
        if self.key is None: #прооверка на пустоту
            print('Tree is empty')
            return
        
        if data < self.key: #если данные меньше корневых, то искать только в левом поддереве, иначе в правом поддереве
            if self.lchild:
                self.lchild = self.lchild.delete2(data,curr)
            else:
                print('Given node in not presented')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete2(data,curr)
            else:
                print('Given node in not presented')
                
        else:
            '''Если данные равны узлу, и узел имеет 1 или 0 потомков'''
            if self.lchild is None: 
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp 
            '''Если данные равны узлу, и узел имеет 2 потомка'''
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete2(node.key,curr)
        return self
    
    def min_node(self):
        '''функция для поиска наименьшего ключа'''
        current = self
        while current.lchild:
            current = current.lchild
        print('min node:\n->', current.key)
        
    def max_node(self):
        '''функция для поиска наибольшего ключа'''
        current = self
        while current.rchild:
            current = current.rchild
        print('min node:\n->', current.key)
        


# In[3]:


def printTree(node, level=0):
    if node != None:
        if node.key is None:
            return 'Tree is empty'
        printTree(node.rchild, level + 1)
        print('  ' * 3 * level , '->' , node.key)
        printTree(node.lchild, level + 1)


# In[4]:


#РАБОТАЕТ С ОДНОЙ ВЕТКОЙ

list = [5,4,3,2,1]

tree = BST(list[0]) 

for i in list[1:]:
    tree.insert(i)

print('Исходное дерево:\n')

printTree(tree)


# In[9]:


tree.delete(5)

print('\nИтоговое дерево:\n')
    
printTree(tree)


# # 1 Часть
# 
# 1.Случайным образом сгенерировать 25 чисел в диапазоне от 1 до 50. 
# Каждое вновь сгенерированное число использовать в качестве ключа при добавлении
# в ДДП. Вывести на экран получившееся дерево (любым удобным для прочтения/интерпретации способом).

# In[60]:


mass = random.sample(range(1, 50), 25)
tree1 = BST(mass[0])
for el in mass[1:]:
    tree1.insert(el)
print(mass)
printTree(tree1)


# # 2.Из получившегося дерева получить отсортированный массив ключей размера 25.

# In[61]:


def sorted_keys(tree, keys):
    if tree is not None:
        sorted_keys(tree.lchild,keys)
        keys.append(tree.key)
        sorted_keys(tree.rchild, keys)

keys = []
sorted_keys(tree1,keys)
print(keys)


# # 3.Повторить пункты 1-2 для 1.000/5.000/10.000 чисел в диапазоне:

# In[62]:


def task_third(rangee):
    for num in [1000, 5000, 10000]:
        start_time = perf_counter()
        mass = [random.randint(1, rangee) for _ in range(num)]
        tree = BST(mass[0])
        for el in mass[1:]:
            tree.insert_any(el)
        keys = []
        sorted_keys(tree, keys)
        
        print(f'Время выполениея для {num} элементов: {perf_counter() - start_time}')


# # a.	от 1 до 10.000
# 

# In[63]:


task_third(10000)


# In[64]:


task_third(500)


# # 4.   Сгенерировать массивы чисел размера 1.000/5.000/10.000 
#     (сначала в диапазоне от 1 до 10.000, потом в диапазоне от 1 до 500).
#     Произвести сортировку массивов с использованием любого алгоритма сортировки
#     (используйте библиотечные функции python), при этом не забудьте произвести
#     замеры времени работы на каждом размере массива. -->
# 

# In[65]:


keys = []
array_time = []

for i in [10000, 500]:
    for j in [1000, 5000, 10000]:
        time_start = perf_counter()
        mas = [randint(1, i) for _ in range(j)]
        tree = BST(mas[0])
        for el in mas[1:]:
            tree.insert(el)
        sorted_keys(tree, keys)
        ttime = perf_counter() - time_start
        array_time.append(ttime)


# In[66]:


df = pd.DataFrame({
'Кол-во эл-тов': ['1000', '5000', '10000', '1000', '5000', '10000',],
'Диапазон': ['1-10000', '1-10000', '1-10000', '1-500', '1-500', '1-500'],
'время выполнения': [array_time[0],array_time[1], array_time[2], array_time[3], array_time[4], array_time[5]]})
df


# # 2 Часть
#  
#  1.Напишите функцию, определяющую высоту дерева. 
#     Продемонстируйте работу этой функции.

# In[67]:


def height_of_tree(node):
    if not node:
        return 0
    return max(height_of_tree(node.lchild), height_of_tree(node.rchild)) + 1

array = [randint(1, 100) for _ in range(25)]

tree = BST(array[0])
for i in array[1:]:
    tree.insert(i)

print(f'Высота ДДП: {height_of_tree(tree)}')

printTree(tree)


# # 2. Сгенерируйте случайным образом ДДП, состоящее из 50 узлов, содержащих 
#     ключи в диапазоне от 1 до 25. Далее пользователь вводит любое число X.
#     В построенной дереве производится удаление всех вершин, у которых ключ 
#     равен X, и вывод получившегося дерева, либо пользователю сообщается, 
#     что вершины с данным ключом X в дереве не существует.

# In[68]:


arr = [randint(1, 50) for i in range(50)]
print(arr)
tre = BST(arr[0])
for i in arr[1:]:
  tre.insert_any(i)
print('Исходное дерево:\n')
printTree(tre)
#исходное дерево


# In[ ]:





# In[70]:


X = int(input('Введите число для удаления\n=>'))

while tre.search(X) != False:
    tre.delete(X)


print('\nИтоговое дерево:\n')
printTree(tre)
#результат


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




