import sys

sys.stdout.reconfigure(encoding='utf-8')


MILLILITERS_PER_KG = 30
MILLILITERS_PER_LITER = 1000

# Приветствие пользователя
print(
    'Здравствуйте, я ваш персональный помощник',
    'по отслеживанию здоровья - FitLife'
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
        user_weight = float(input('Укажите ваш вес (в килограммах) - '))
        break
    except ValueError:
        print('Вес должен быть числом.')

# Запрашиваем рост пользователя

while True:
    try:
        user_height = float(input('Укажите ваш рост в метрах '
                                  '(например 1.82) - '))
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
last_digit = user_age % 10

if 11 <= user_age <= 14:
    age_suffix = 'лет'
elif last_digit == 1:
    age_suffix = 'год'
elif last_digit == 2 or last_digit == 3 or last_digit == 4:
    age_suffix = 'года'
else:
    age_suffix = 'лет'


print(f'Ответ для пользователя: {user_name} ({user_age} {age_suffix})')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_l:.2f} л. в день', end='\n\n')
print('Рассчет окончен. Будьте здоровы!')


# ИИ использовал только для того чтобы узнать про try и except
# (узнал про устройство этой конструкции в целом, а не получил готовый код)
# и у меня не проходился 1 тест, что-то с котировкой было - узнал у чатагпт
# и он сказал первые 2 строчки добавить, указав котировку явно.
# а так больше ИИ нигде нет
