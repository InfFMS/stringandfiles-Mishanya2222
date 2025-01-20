# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.

with open('task2.txt', 'r', encoding='utf-8') as f:
    fl = f.readlines()



n = ''
x = 0
for i in fl:
    x = x + i.count('Python')
    n = n + i

print('количество замен',x)
n = n.replace('Python', 'Питон')
d = open('new-file2.txt', 'w', encoding='utf-8')
d.write(n)
d.close()