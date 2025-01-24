# Grade 2. Этап 2.5 Удаление заметок.
# Добавьте функциональность для удаления заметки по имени пользователя или заголовку.

# Создаем список заметок
notes = [
    {
        'id': 1,
        'username': 'Дмитрий',
        'title': 'ДР сестры',
        'description': 'Купить подарок'
    },
    {
        'id': 2,
        'username': 'Милена',
        'title': 'Дальнейшее обучение',
        'description': 'Выбрать учебное заведение'
    },
    {
        'id': 3,
        'username': 'Юлия',
        'title': 'Лечение',
        'description': 'Прием у врача'
    }
]

# Вывод текущего списка заметок
print("Текущие заметки:")
for note in notes:
    print(f"{note['id']}. Имя: {note['username']}")
    print(f"   Заголовок: {note['title']}")
    print(f"   Описание: {note['description']}\n")

# Запускаем цикл запроса на удаление заметки
while True:
    # Запрос критерия для удаления
    search_term = input("Введите имя пользователя или заголовок для удаления заметки: ")
    search_term = search_term.capitalize()

    # Проверка, что ввод не пустой
    if not search_term:
        print("Ошибка: критерий поиска не может быть пустым.")
        continue

    # Добавляем функционал для завершения цикла
    elif search_term == "" or search_term.capitalize() == "Стоп":
        break
    # Создаем новый список для хранения заметок, которые нужно оставить
    else:
        notes_to_keep = []
        notes_to_delete = []

        # Поиск заметок для удаления
        for note in notes:
            # Если ключевые слова совпадают, добавляет заметку в список для удаления
            if note['username'] == search_term or note['title'] == search_term:
                notes_to_delete.append(note)
            # В ином случае - в список для сохранения
            else:
                notes_to_keep.append(note)

        # Проверка, найдены ли заметки в списке для удаления
        # В случае если таковых не найдено запускаем цикл заново
        if not notes_to_delete:
            print("Заметок с таким именем пользователя или заголовком не найдено.")
            continue

        else:
            # Вывод заметок, которые будут удалены
            print("\nСледующие заметки будут удалены:")

            for note in notes_to_delete:
                print(f"{note['id']}. Имя: {note['username']}")
                print(f"   Заголовок: {note['title']}")
                print(f"   Описание: {note['description']}\n")


        while True:
            # Запрос подтверждения удаления
            confirm = input("Вы уверены, что хотите удалить эти заметки? (да/нет): ")

            if confirm.capitalize() == 'Да':
                # Обновление списка заметок
                notes = notes_to_keep

                # Обновление ID заметок
                for i, note in enumerate(notes, 1):
                    note['id'] = i

                # Вывод результата
                print("\nЗаметки успешно удалены.")

                if notes:
                    print("\nОстались следующие заметки:")

                    for note in notes:
                        print(f"{note['id']}. Имя: {note['username']}")
                        print(f"   Заголовок: {note['title']}")
                        print(f"   Описание: {note['description']}\n")
                #В случае если все заметки удалены уведомляем об этом пользователя
                else:
                    print("Список заметок пуст.")
                break
            # В случае если
            elif confirm != "Да" or confirm != "Нет":
                print('Некорректный ввод! Введите "Да" или "Нет"')
                continue

            else:
                print("\nУдаление отменено.")
                continue

