username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гггг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гггг': ")


title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title1.capitalize(), title2.capitalize(), title3.capitalize()]


print("\nВы ввели следующие данные:")
print("Имя пользователя:", username.title())
print("Заголовки заметки:", titles)
print("Описание заметки:", content.capitalize())
print("Статус заметки:", status.capitalize())
print("Дата создания:", created_date [:5])
print("Дата истечения:", issue_date [:5])
