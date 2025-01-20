# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.


with open('task5.txt', 'r', encoding='utf-8') as f:
    fl = f.readlines()

a = ''
max = 1
newfl = ''
for i in fl:
    t= i.replace('!','').lower()
    t= t.replace('.', '')
    t= t.replace('\n', ' ').split()
    print(t)
    for j in t:
        if max < len(j):
            max = len(j)
            a = j
print(f'слово: {a},' ,f'длина: {max}')

HH = f'слово: {a},'  + f' длина: {max}'

d = open('new-file5.txt', 'w', encoding='utf-8')
d.write(HH)
d.close()

