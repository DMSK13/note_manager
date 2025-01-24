# Grade 2. Этап 2.3 Обработка дедлайнов.
# Задание: Обработка дедлайнов.
# Проверьте, истек ли срок выполнения заметки (issue_date), и выведите предупреждение, если дедлайн прошел.


# Импортируем необходимые модули для работы с датами
from datetime import datetime
# Выводим текущую дату
print("Текущая дата:", datetime.now().strftime("%d-%m-%Y"))
# Основной блок программы
while True:
    try:
        # Запрашиваем дату дедлайна у пользователя
        deadline_str = input("Введите дату дедлайна (в формате день-месяц-год, например 17-01-2025): ")

        # Преобразуем строку с датой в объект datetime
        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y")

        # Вычисляем разницу между текущей датой и дедлайном
        current_date = datetime.now()
        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        # Проверяем статус дедлайна и выводим соответствующее сообщение
        if days_difference < 0:
            print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference:02d} дней.")

        # Прерываем цикл после успешной обработки даты
        break

    except ValueError:
        # Обработка ошибки неверного формата даты
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 17-01-2025")

    except Exception as e:
        # Обработка прочих ошибок
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")
