from collections import Counter
from string import punctuation


def signs_deleter(content):
    new_content = ''
    for letter in content:
        if letter not in punctuation and letter != '\n':
            new_content += letter.lower()
    return new_content


def word_counter(content):
    return len(content.split(' '))


def duplicated_counter(content):
    return Counter(content.split(' '))


def run():
    with open(file, 'r') as file:
        content = file.read()
    new_content = signs_deleter(content)

    print('Liczba liter to: ', word_counter(new_content))
    print('10 najczęściej używanych słów to: ', duplicated_counter(new_content).most_common(10))
