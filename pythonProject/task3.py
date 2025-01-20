# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.

with open('task3.txt', 'r', encoding='utf-8') as f:
    fl = f.readlines()

nn = ''
xx = 0
for h in fl:
    xx = xx + h.count('Python')
    nn = nn + h
nn = nn.lower()

newfl = ''
for i in fl:
    t= i.replace(',','').lower()
    t= t.replace('.', '')
    t= t.replace('\n', ' ').split()
    print(t)
    for j in t:
        newfl = newfl + j +':' + f"{nn.count(j)}" + "\n"

d = open('new-file3.txt', 'a', encoding='utf-8')
d.write(newfl)
d.close()
