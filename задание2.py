# Есть строка letters. Нужно пройтись по каждому символу строки с помощью цикла и:

# Посчитать количество символов равных значению переменной template
# Вывести все символы, не равные значению exclude
# Для теста можно использовать:

# letters = 'Who keeps company with the wolf, will learn to howl.'
# template = 'w'
# exclude = 'l'


letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'
counter_template = 0
not_exclude = ''

for i in letters:

    if i == template:
        counter_template = counter_template + 1
    if i != exclude:
        not_exclude = not_exclude + i

print('количество в тексте "', template ,'"', counter_template)
print('исходный текст :',letters)
print('опущенны "',exclude ,'" :' , not_exclude)
