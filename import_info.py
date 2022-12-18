import csv


def create_data(text: str):
    """Добавление нового контакта"""
    text = list(text.split())
    with open('data_base.csv', 'a', newline= '', encoding='UTF-8') as file:
        data = csv.writer(file)
        data.writerow(text)
        print('Информация внесена')


def delete_data(text: str):
    """Удаление контакта"""
    with open('data_base.csv', 'r', encoding="UTF-8") as file:
        data_base = csv.reader(file)
        res_list = []
        us_list = list(text.split())
        for line in data_base:
            count = 0
            if us_list[count] in line:
                for el in line:
                    if us_list[count] == el:
                        count += 1
                        if len(us_list) > count:
                            for it in line:
                                if us_list[count] == it:
                                    count += 1
                                    if len(us_list) > count:
                                        for it_1 in line:
                                            if us_list[count] == it_1:
                                                count += 1
                                                if len(us_list) > count:
                                                    for it_2 in line:
                                                        if us_list[count] != it_1:
                                                            count -= 1
                                                count -= 1
                                    count -= 1
                        count -= 1
                    count = 0
            else:
                res_list.append(line)

    with open('data_base.csv', 'w', newline= '', encoding='UTF-8') as out:
        csv_writer = csv.writer(out)
        for row in res_list:
            csv_writer.writerow(row)

    return res_list
