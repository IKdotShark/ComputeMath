""" 9 Лабораторная - реализовать структуру данных - дерево
задать рандомно дерево и посчитать его наибольшую глубину.

insert(self, key): Метод для вставки нового узла с ключом key в красно-черное дерево.
Проверяет, есть ли корневой узел, и вставляет новый узел с соответствующим ключом
в соответствии с правилами дерева. Затем вызывает метод fix_tree.

fix_tree(self, node): Метод для коррекции красно-черного свойства дерева
после вставки нового узла. Осуществляет перебалансировку и перекрашивание узлов,
чтобы удовлетворить правила красно-черного дерева.

random_insert(self, num_nodes): Метод для случайной вставки заданного количества узлов в дерево.
Генерирует случайные ключи узлов и вставляет их в дерево с помощью метода insert.

get_max_depth(self): Метод для получения максимальной глубины дерева.
Вызывает вспомогательный метод __get_max_depth_helper и возвращает максимальную глубину дерева.

__get_max_depth_helper(self, node): Вспомогательный метод для рекурсивного подсчета
максимальной глубины дерева, начиная с узла node.
Возвращает максимальную глубину дерева от узла node."""
# Импорт необходимых модулей
from termcolor import colored
import random

class Node:
    def __init__(self, key, red=True):
        self.key = key
        self.red = red
        self.left = None
        self.right = None
        self.parent = None

class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            node.red = False
            self.root = node
            return
        current = self.root
        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.left = None
        node.right = None
        self.fix_tree(node)

    def fix_tree(self, node):
        print('NODE PARENT RED - {}'.format(node.parent.red))
        try:
            while node.parent.red is True and node is not self.root:
                print('ФИКС>> КЛЮЧ УЗЛА - {} '
                      'КЛЮЧ РОДИТЕЛЯ - {}'.format(node.key,
                                                     node.parent.key))
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    print('[ЛЕВЫЙ] ДЯДЯ КРАСНЫЙ - {} '
                          'КЛЮЧ ДЯДИ - {} РОДИТЕЛЬ РОДИТЕЛЯ {}'.format(uncle.red, uncle.key, node.parent.parent.key))
                    if uncle.red:
                        '''
                        Вставка нового узла, когда родитель и дядя красные
                        -> неверно
                        Перекрашиваем родителя и дядю в черный цвет
                        '''
                        node.parent.red = False
                        uncle.red = False
                        node.parent.parent.red = True
                        node = node.parent.parent
                        print('ЦВЕТ УЗЛА - {} ЦВЕТ ДЯДИ - {} ЦВЕТ РОДИТЕЛЯ - '
                              '{}'.format(
                                    colored(node.red, 'red',
                                            attrs=['reverse', 'blink']),
                                    colored(uncle.red, 'yellow',
                                            attrs=['reverse', 'blink']),
                                    colored(node.parent.red, 'yellow',
                                            attrs=['reverse', 'blink'])))
                    else:
                        if node == node.parent.right:
                            # Это случай 2
                            print('в ТЕСТ>>>>', node.key)
                            node = node.parent
                            print('ПОСЛЕ ТЕСТА>>>>', node.key)

                            # self.left_rotate(node)
                        # Это случай 3
                        # node.parent.red = False
                        # node.parent.parent.red = True
                        # self.right_rotate(node.parent.parent)

                else:
                    try:
                        uncle = node.parent.parent.left
                        print('[ПРАВЫЙ] ДЯДЯ КРАСНЫЙ - {} '
                              'КЛЮЧ ДЯДИ - {}'.format(uncle.red, uncle.key))
                        if uncle.red:
                            #  Случай 1
                            node.parent.red = False
                            uncle.red = False
                            node.parent.parent.red = True
                            print('ЦВЕТ УЗЛА - {} ЦВЕТ ДЯДИ - {} ЦВЕТ РОДИТЕЛЯ - '
                                  '{}'.format(
                                        colored(node.red, 'red',
                                                attrs=['reverse', 'blink']),
                                        colored(uncle.red, 'yellow',
                                                attrs=['reverse', 'blink']),
                                        colored(node.parent.red, 'yellow',
                                                attrs=['reverse', 'blink'])))

                    except AttributeError:
                        print("НЕТ ДЯДИ")
                        break

            self.root.red = False
        except AttributeError:
            print("\n\nДерево ПОСТРОЕНО")

    def random_insert(self, num_nodes):
        keys = random.sample(range(1, num_nodes * 10), num_nodes)
        for key in keys:
            self.insert(key)

    def get_max_depth(self):
        return self.__get_max_depth_helper(self.root)

    def __get_max_depth_helper(self, node):
        if node is None:
            return 0
        left_depth = self.__get_max_depth_helper(node.left)
        right_depth = self.__get_max_depth_helper(node.right)
        return max(left_depth, right_depth) + 1

# Пример использования
rb_tree = RBTree()
rb_tree.random_insert(10)
max_depth = rb_tree.get_max_depth()
print(f"Максимальная глубина дерева: {max_depth}")