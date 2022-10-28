from operator import itemgetter
'''
Вариант Г

«Язык программирования» и «Синтаксическая конструкция» связаны соотношением один-ко-многим. 
Выведите список всех языков программирования, у которых название начинается с буквы «П», и список содержащих в них синтаксической конструкции.

«Язык программирования» и «Синтаксическая конструкция» связаны соотношением один-ко-многим. 
Выведите список языков программирования с максимальной сложностью синтаксических конструкции в каждом языке программирования, отсортированный по максимальной сложности.

«Язык программирования» и «Синтаксическая конструкция» связаны соотношением многие-ко-многим. 
Выведите список всех связанных языков программирования и синтаксических конструкций, отсортированный по языками, сортировка по синтаксической конструкции произвольная. 
'''

# класс - Синтаксическая конструкция
class Syntactic_construction:
    def __init__(self, id, name, complexity, Programming_language_id):
        # номер синтаксического конструкции
        self.id = id
        # название синтаксического конструкции
        self.name = name
        # сложность на которой находится синтаксическая конструкция
        self.complexity = complexity
        # номер языков программирования
        self.Programming_language_id = Programming_language_id

# класс - Язык программирования
class Programming_language:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# классы - Язык программирования и Синтаксическая конструкция
class Syntactic_construction_Programming_language:
    def __init__(self, Programming_language_id, Syntactic_construction_id):
        self.Programming_language_id = Programming_language_id
        self.Syntactic_construction_id = Syntactic_construction_id

Programming_language_s = [
    Programming_language(1, 'Джава скрипт'),
    Programming_language(2, 'Пхп'),
    Programming_language(3, 'Питон'),
    Programming_language(4, 'Свифт'),
    Programming_language(5, 'Kотлин')
]
Syntactic_construction_s = [
    Syntactic_construction(1, 'Легко', 10, 1),
    Syntactic_construction(2, 'Немножко среднее', 20, 3),
    Syntactic_construction(3, 'Среднее', 30, 2),
    Syntactic_construction(4, 'Немножко сложно', 40, 4),
    Syntactic_construction(5, 'Сложно', 50, 5),
    Syntactic_construction(6, 'Сверхсложно', 60, 1)
]
Syntactic_construction_s_of_Programming_language_s = [
    Syntactic_construction_Programming_language(3, 1),
    Syntactic_construction_Programming_language(4, 2),
    Syntactic_construction_Programming_language(5, 3),
    Syntactic_construction_Programming_language(1, 4),
    Syntactic_construction_Programming_language(2, 5),
    Syntactic_construction_Programming_language(6, 6),
]

def main():
    one_to_many = [(ch.name, ch.complexity, Programming_language.name)
                   for Programming_language in Programming_language_s
                   for ch in Syntactic_construction_s
                   if ch.Programming_language_id == Programming_language.id]

    many_to_many_temp = [(Programming_language.name, ChOfProgramming_language_s.Programming_language_id, ChOfProgramming_language_s.Syntactic_construction_id)
                         for Programming_language in Programming_language_s
                         for ChOfProgramming_language_s in Syntactic_construction_s_of_Programming_language_s
                         if Programming_language.id == ChOfProgramming_language_s.Programming_language_id]

    many_to_many = [(ch.name, ch.complexity, Programming_language_name)
                    for Programming_language_name, Programming_language_id, ch_id in many_to_many_temp
                    for ch in Syntactic_construction_s if ch.id == ch_id]

    print('')
    print('Задание Г_1 - начинается с П')
    array_dict = {}
    for lib_name, x, Programming_language_name in one_to_many:
        # если название языков программирования начинается с 'А'
        if Programming_language_name[0] == 'П':
            if Programming_language_name in array_dict:
                array_dict[Programming_language_name].append(lib_name)
            else:
                array_dict[Programming_language_name] = [lib_name]
    print(*array_dict.items())

    print('')
    print('Задание Г_2 - номер по максимальной сложности')
    array_dict_2 = {}
    for x, func_num, Programming_language_name in one_to_many:
        if Programming_language_name in array_dict_2:
            array_dict_2[Programming_language_name] = max(array_dict_2[Programming_language_name], func_num)
        else:
            array_dict_2[Programming_language_name] = func_num
    array_dict_2 = {key: value for key, value in sorted(array_dict_2.items(), key=lambda item: item[1])}
    print(*array_dict_2.items())

    print('')
    print('Задание Г_3 - отсортированный по языками, сортировка по синтаксической конструкции произвольная')
    array_list = []
    for lib_name, x, Programming_language_name in many_to_many:
        array_list.append((Programming_language_name, lib_name))
    array_list = sorted(array_list, key=lambda item: item[0])
    print(*array_list)

if __name__ == '__main__':
    main()