# python main.py input_json.txt input.txt output.txt

import argparse
from Labs.validator import val
from Labs.sort import sort_menu

parser = argparse.ArgumentParser()
parser.add_argument('input_json')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()


print("Выберите дейтсвие:")
print("1. Отвалидировать записи в исходном файле.")
print("2. Отсортировать записи в файле с валидными данными.")
print("3. Выход.")

while True:
    choice = input(">> ")
    if choice == '1':
        val(args.input_json, args.input)
        break
    elif choice == '2':
        sort_menu(args.input, args.output)
        break
    elif choice == '3':
        print("ок..")
        break
    else:
        print("Неверно")
# data = json.load(open(args.input_json, encoding='utf-8'))
# pickle.dump(data, open(args.input, "wb"))
# data = pickle.load(open(args.input, "rb"))
# Сортировка записей по возрасту
# bubble_sort(data)
# print(data)
# pickle.dump(data, open(args.input, "wb"))
