# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


# не работает:
def pers_info(**kwargs):
    print(f"{kwargs['name']} {surname} {b_year} года рождения, "
          f"проживает в г {hometown}, email: {email}, тел: {phone}")

pers_info(name = "Ivan", surname = "Ivanov" ,b_year = "1991" , hometown = "Ivanovo", email = "Ivan@email.com", phone = "1234554321")

# работает:
def pers_func(name, surname, b_year, hometown, email, phone):
    print(name, surname, b_year, hometown, email, phone)

pers_func(name= 'Ivan', surname='Ivanov', b_year=1991, hometown='Ivanovo', email='Ivan@email.com', phone='1234554321')