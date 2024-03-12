from src.classes import user_choice_hh

def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    print('Добро пожаловать! С помощью данной программы вы можете найти подходящую вакансию на сайте HeadHunter. \n'
          'Чтобы продолжить введите "Начать".\n'
          'Чтобы выйти из программы введите "Выход".\n')

    while True:
        user_choice_platform = input()
        if user_choice_platform == 'Начать':
            print('HeadHunter')
            user_choice_hh()
            break
        elif user_choice_platform == 'Выход':
            print('До встречи')
            break
        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    user_interaction()