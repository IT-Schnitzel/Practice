# Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
# Реализовать одну функцию, которая выполняет следующие операции:
# - прочитать файл построчно;
# - непустые строки добавить в список;
# - удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
# - объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
# - создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
#   где ключом будет уникальное слово, а значением - количество;
# - вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
#   (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
# - заменить все эти слова в строке на слово “PYTHON”;
# - создать новый txt-файл;
# - записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
#   при этом не делить слова.
import re
def wiki_function():
    words_dict = {}
    clean = []
    file = open("Wiki.txt", 'r')
    for line in file:
        if line.strip():
            clean_l = re.sub(r'[^a-zA-Z\s]', '', line)
            words = clean_l.split()
            clean.extend(words)

    for word in clean:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    sorted_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    replaced_text = ' '.join(clean)
    i = 1
    for word, _ in sorted_words[:10]:
      print(str(i) + " place ---" + str(word) + "--- " + str(clean.count(word)) + " times")
      replaced_text = replaced_text.replace(" " + str(word) + " ", ' PYTHON ')
      i = i+1
    new_f = open('Wiki2.txt', 'w')
    line_length = 0
    for word in replaced_text.split():
        if ((line_length + len(word)) <= 100):
            new_f.write(word + ' ')
            line_length += len(word) + 1
        else:
            new_f.write('\n' + word + ' ')
            line_length = len(word) + 1
    new_f1 = open('Wiki2.txt', 'r')
    for line in new_f1:
      print(line.strip())


wiki_function()
