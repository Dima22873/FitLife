import sys

sys.stdout.reconfigure(encoding='utf-8')


MILLILITERS_PER_KG = 30
MILLILITERS_PER_LITER = 1000

# Приветствие пользователя
print(
    'Здравствуйте, я ваш персональный помощник '
    'по отслеживанию здоровья - FitLife',
)

# Запрашиваем Имя пользователя
user_name = input('Как вас зовут? - ')

# Запрашиваем возраст пользователя
while True:
    try:
        user_age = int(input('Укажите ваш возраст - '))
        break
    except ValueError:
        print('Возраст должен быть целым числом.')

# Запрашиваем вес пользователя
while True:
    try:
        user_weight = float(
            input('Укажите ваш вес (в килограммах) - ').replace(',', '.')
        )
        break
    except ValueError:
        print('Вес должен быть числом.')

# Запрашиваем рост пользователя

while True:
    try:
        user_height = float(
            input(
                'Укажите ваш рост в метрах '
                '(например 1.82) - ').replace(',', '.')
        )
        break
    except ValueError:
        print('Рост должен быть числом.')

# Рассчет ИМТ
bmi = user_weight / (user_height**2)

# Рассчет нормы воды(в миллилитрах)
water_ml = user_weight * MILLILITERS_PER_KG

# Переводим миллилитры в литры
water_l = water_ml / MILLILITERS_PER_LITER


# Проверка приставки после возраста пользователя
def get_age_suffix(age):
    """Возвращает правильно оконцание для возраста."""
    last_digit = age % 10

    if 11 <= age <= 14:
        return 'лет'
    elif last_digit == 1:
        return 'год'
    elif last_digit == 2 or last_digit == 3 or last_digit == 4:
        return 'года'
    else:
        return 'лет'


age_suffix = get_age_suffix(user_age)

print(
    f'Ответ для пользователя: {user_name} ({user_age} {age_suffix})\n'
    f'Твой Индекс Массы Тела: {round(bmi, 1)}\n'
    f'Рекомендуемая норма воды: {water_l:.2f} л. в день\n\n'
    f'Рассчет окончен. Будьте здоровы!'
)
