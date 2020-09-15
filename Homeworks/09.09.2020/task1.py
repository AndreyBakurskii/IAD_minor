def separate_for_sentences(text: str):

    end = set()
    end.add("!")
    end.add("?")
    sentences_and_ending = dict()
    sentence = ""

    flag_troetochie = 1

    for ind, elem in enumerate(text):
        if flag_troetochie == 2:
            flag_troetochie += 1
            continue

        if flag_troetochie == 3:
            flag_troetochie = 1
            continue

        if elem in end:
            sentences_and_ending[sentence] = elem
            sentence = ""

        elif elem == ".":
            try:
                # проверка троеточия
                if text[ind + 1] == "." and text[ind + 2] == ".":
                    sentences_and_ending[sentence.strip()] = elem + text[ind + 1] + text[ind + 2]
                    sentence = ""
                    flag_troetochie += 1
                # обработка ситуации, когда это не троиточие и не конец текста
                else:
                    sentences_and_ending[sentence.strip()] = elem
                    sentence = ""
            # обработка ошибки, когда это не троеточие, а точка и конец текста
            except IndexError:

                sentences_and_ending[sentence.strip()] = elem
                sentence = ""

        elif elem == ",":
            sentence += ""

        else:
            sentence += elem

    return sentences_and_ending  # ключи это предложения, значение знак окончания предложения


def count_words(sentences_and_ending: dict):

    counter = 0

    for sentence in sentences_and_ending:

        if sentence != "":
            counter += len(sentence.split(" "))

    return counter


def reverse_words_in_sentences(sentences_and_ending: dict):

    reversed_sentences = [" ".join(sentence.split(" ")[::-1]) + ending for sentence, ending in sentences_and_ending.items()]

    return " ".join(reversed_sentences)


def top_10_repeat_words(sentences_and_ending: dict):

    words = dict()  # словарь с ключами в виде слов, значения - их количество в тексте

    for sentence in sentences_and_ending:
        for word in sentence.split(" "):
            if word in words:
                words[word] += 1

            else:
                words[word] = 1

    words = sorted(words, key=words.get, reverse=True)

    return [word for word in words][:10]


with open("file.txt", "r") as f:

    data_file = [line.strip() for line in f.readlines()]  # delete special symbol (\n,\t ...)

data_file = "".join(data_file)

sentences_and_ending = separate_for_sentences(data_file)


print("Count of words:", count_words(sentences_and_ending))
print("Top 10 repeated words:", ", ".join(top_10_repeat_words(sentences_and_ending)))
print("Reversed text:", reverse_words_in_sentences(sentences_and_ending))

