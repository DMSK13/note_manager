username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гггг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гггг': ")


titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title.capitalize())


print("\nВы ввели следующие данные:")
print("Имя пользователя:", username.capitalize())
print("Заголовки заметки:", titles)
print("Описание заметки:", content.capitalize())
print("Статус заметки:", status.capitalize())
print("Дата создания:", created_date [0:5])
print("Дата истечения:", issue_date [0:5])
