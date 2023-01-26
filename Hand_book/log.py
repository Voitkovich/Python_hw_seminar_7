import choice
import find

import datetime

def log(button):

    with open('log.txt', 'a',encoding='utf-8') as file:
        file.write(f'{button}.Время запороса: {str(datetime.datetime.now())} \n')


def log_to_file(contact):

    with open('stroka.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('spisok.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n\n')


def reading_file(param):

    b = find.sep()
    if b == 1:
        with open('stroka.txt', 'r') as file:
            for line in file:
                if param in line:
                    print(line)

    if b == 2:
        list = []
        with open('stroka.txt', 'r') as file:  
            for line in file:
                if param in line:
                    list = line.split(';')
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n')


def reading_all():

    b = find.sep()
    if b == 1:
        with open('stroka.txt', 'r') as file:
            for line in file:
                print(line)
    if b == 2:
        with open('spisok.txt', 'r') as file:
            for line in file:
                print(line)