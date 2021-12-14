import pickle
from tqdm import tqdm


def bubble_sort(data, field):
    with tqdm(total=len(data)) as progressbar:
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if float(data[j][field]) > float(data[j + 1][field]):
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
                progressbar.update(1)


def sort_menu(path_input, path_output):
    sort_data = pickle.load(open(path_input, "rb"))
    print("Доступные поля для сортировки: Рост, ИНН, Номер паспорта, Возраст")
    print("Введите поле по которому будет проводиться сортировка:")
    while True:
        field_choice = input(">> ")
        if field_choice == 'Рост':
            bubble_sort(sort_data, 'height')
            break
        elif field_choice == 'ИНН':
            bubble_sort(sort_data, 'inn')
            break
        elif field_choice == 'Номер паспорта':
            bubble_sort(sort_data, 'passport_number')
            break
        elif field_choice == 'Возраст':
            bubble_sort(sort_data, 'age')
            break
        else:
            print("Неверно")
    pickle.dump(sort_data, open(path_output, "wb"))
    print("Готово!")
    print(f"Записи сохранены в файл: {path_output}")

