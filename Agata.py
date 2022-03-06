from typing import TextIO

file: TextIO = open('C://Users//Agata//Desktop//rolling_stones.txt', "r")

number_of_words = 0

with open(r'C://Users//Agata//Desktop//rolling_stones.txt','r') as file:
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)

print(number_of_words)

