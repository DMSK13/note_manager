# Grade 2. Этап 2.4 Работа с несколькими заметками.
# Задание: Работа с несколькими заметками.
# Реализуйте возможность создания и хранения нескольких заметок в списке.
from datetime import datetime

# Создаём пустой список заметок
notes = []

print("\nДобро пожаловать в менеджер заметок!")
# Запускаем цикл приёма ответа от пользователя
while True:
    user_answer = input("Создать новую заметку? (Да\Нет)")
    # При отрицательном ответе завершаем программу
    if user_answer.capitalize().strip() == "Нет":

        break
    # При положительном ответе собираем информацию о заметке от пользователя
    elif user_answer.capitalize().strip()  == "Да":
        heading = ["username", "title", "description", "status", "created_date", "deadline_date"]
        username = input("Введите имя пользователя: ")
        content = input("Введите заголовок заметки: ")
        description = input("Введите описание заметки: ")
        # Запускаем цикл сбора информации о статусе заметки
        while True:
            # Создаём словарь включающий варианты статусов
            note_status = {1: 'новая', 2: 'в процессе', 3: 'выполнено'}

            # Выводим на экран перечень доступных статусов
            print("Выберите статус заметки: ")
            print("\n1 -", note_status[1], "\n2 -", note_status[2], "\n3 -", note_status[3])

            status = input("Введите код статуса: ")

            if status == "1":
                status = note_status[1]
                break

            elif status == "2":
                status = note_status[2]
                break

            elif status == "3":
                status = note_status[3]
                break

            else:
                print("Неверный код! Введите корректный числовой код статуса из нижеперечисленного перечня.")
        #
        while True:

            try:

                input_date = input('Введите дату создания (ДД-ММ-ГГГГ): ')
                created_tmp = datetime.strptime(input_date, "%d-%m-%Y")

                if created_tmp == datetime.strptime(input_date, "%d-%m-%Y"):
                    created_date = created_tmp

                    break

                else:
                    print("Некорректный ввод! Введите дату создания в формате ДД-ММ-ГГГГ")



            except ValueError:
                print("Введена некорректная дата, попробуйте ещё раз.")

            except Exception as e:
                # Обработка прочих ошибок
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова.")
        #
        while True:

            try:
                input_deadline = input('Введите дату дедлайна (ДД-ММ-ГГГГ): ')
                deadline_tmp = datetime.strptime(input_deadline, "%d-%m-%Y")

                if deadline_tmp <= created_tmp:
                    print("Некорректный ввод! Дата дедлайна не может быть меньше даты создания")

                    continue
                elif deadline_tmp == datetime.strptime(input_deadline, "%d-%m-%Y"):
                    deadline_date = deadline_tmp

                    break
                else:
                    print("Некорректный ввод! Введите дату создания в формате ДД-ММ-ГГГГ")

            except ValueError:
                print("Введена некорректная дата, попробуйте ещё раз.")

            except Exception as e:
                # Обработка прочих ошибок
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова.")

        note_data = [username.capitalize(), content.capitalize(),
                     description.capitalize(), status.capitalize(),
                     created_date.strftime("%d-%m-%Y"),
                     deadline_date.strftime("%d-%m-%Y")]
        note = dict(zip(heading, note_data))
        notes.append(note)
    #
    elif user_answer.capitalize() != "Да" or user_answer.capitalize() != "Нет":
        print("Некорректный ответ! Введите 'Да' или 'Нет'")
        continue

# Выводим список созданных заметок на экран
counter = 1

for note in notes:
    print(f"Заметка {counter}.")
    print(f"        Имя: {note['username']}")
    print(f"        Заголовок: {note['title']}")
    print(f"        Описание: {note['description']}")
    print(f"        Статус: {note['status']}")
    print(f"        Дата создания: {note['created_date']}")
    print(f"        Дедлайн: {note['deadline_date']}")
    counter = counter + 1


