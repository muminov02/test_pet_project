# pip install mysql-connector-python
from mysql.connector import connect, Error


def get_data():
    try:
        job_title = input("Наименование вакансии: ")
        key_skills = input("Ключевые навыки: ")
        description = input("Описание: ")
        salary = int(input("Зарплата: "))
        work_type = input("Вид работы (удаленный, смешанный, в офисе): ")
        save_data = (job_title, key_skills, description, salary, work_type)
        return save_data
    except:
        print("Что-то пошло не так попробуйте ещё раз")


def insert_data():
    try:
        with connect(
            host="localhost",
            user='root',
            password='root',
            database="test",
        ) as connection:

            insert_query = """
            INSERT INTO test (job_title, key_skills, description, salary, work_type)
            VALUES
                (%s, %s, %s ,%s, %s)
            """
            data = get_data()
            with connection.cursor() as cursor:
                cursor.execute(insert_query, data)
                connection.commit()

    except Error as e:
        print(e)


def find_data():

    data = (input("Введите имя вакансии: "),)

    try:
        with connect(
            host="localhost",
            user='root',
            password='root',
            database="test",
        ) as connection:

            select_query = """
            SELECT job_title, key_skills, description, salary, work_type
            FROM test
            WHERE job_title LIKE %s
            ORDER BY job_title
            """

            with connection.cursor() as cursor:
                cursor.execute(select_query, data)
                for job in cursor.fetchall():
                    print(job)

    except Error as e:
        print(e)


# find_data()
insert_data()
