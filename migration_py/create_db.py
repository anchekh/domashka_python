from app import app, db
from models import Student

def add_student(last_name, first_name, surname, email):
    student = Student(
        last_name=last_name,
        first_name=first_name,
        surname=surname,
        email=email
    )
    db.session.add(student)

def populate_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        students_data = [
            ("Афанасьев", "Иван", "Евгеньевич", "afanasevie23@vvsu.ithub.ru"),
            ("Баковский", "Егор", "Анатольевич", "bakovskiyea23@vvsu.ithub.ru"),
            ("Бондарчук", "Павел", "Романович", "bondarchukpr23@vvsu.ithub.ru"),
            ("Ваганова", "Инесса", "Андреевна", "vaganovaia23@vvsu.ithub.ru"),
            ("Горпенюк", "Максим", "Александрович", "gorpenyukma23@vvsu.ithub.ru"),
            ("Дубровин", "Антон", "Андреевич", "dubrovinaa23@vvsu.ithub.ru"),
            ("Каратеева", "Полина", "Александровна", "karateevapa23@vvsu.ithub.ru"),
            ("Кнышов", "Данила", "Александрович", "knyshovda23@vvsu.ithub.ru"),
            ("Коваль", "Даниил", "Васильевич", "kovaldv23@vvsu.ithub.ru"),
            ("Кочетов", "Роман", "Владимирович", "kochetovrv23@vvsu.ithub.ru"),
            ("Кошеватый", "Егор", "Павлович", "koshevatyyep23@vvsu.ithub.ru"),
            ("Кравченко", "Дмитрий", "Александрович", "kravchenkoda23@vvsu.ithub.ru"),
            ("Кулигин", "Андрей", "Александрович", "kuliginaa23@vvsu.ithub.ru"),
            ("Курочкина", "Вероника", "Евгеньевна", "kurochkinave23@vvsu.ithub.ru"),
            ("Латышев", "Глеб", "Вадимович", "latyshevgv23@vvsu.ithub.ru"),
            ("Маковский", "Макар", "Дмитриевич", "makovskiymd23@vvsu.ithub.ru"),
            ("Мишин", "Богдан", "Валерьевич", "mishinbv23@vvsu.ithub.ru"),
            ("Нихаенко", "Алиса", "Александровна", "nikhaenkoaa23@vvsu.ithub.ru"),
            ("Павлушко", "Виолетта", "Максимовна", "pavlushkovm23@vvsu.ithub.ru"),
            ("Панькова", "Варвара", "Андреевна", "pankovava23@vvsu.ithub.ru"),
            ("Плясова", "Дарья", "Вадимовна", "plyasovadv23@vvsu.ithub.ru"),
            ("Романов", "Иван", "Евгеньевич", "romanovie23@vvsu.ithub.ru"),
            ("Службин", "Кирилл", "Максимович", "sluzhbinkm23@vvsu.ithub.ru"),
            ("Стройлов", "Александр", "Алексеевич", "stroylovaa23@vvsu.ithub.ru"),
            ("Тем", "Евгений", "Владимирович", "temev23@vvsu.ithub.ru"),
            ("Тен", "Анатолий", "Сергеевич", "tenas23@vvsu.ithub.ru"),
            ("Чиж", "Вячеслав", "Аркадьевич", "chizhva23@vvsu.ithub.ru"),
            ("Швецова", "Белла", "Витальевна", "shvetsovabv23@vvsu.ithub.ru"),
            ("Юдина", "Лейла", "Андреевна", "yudinala23@vvsu.ithub.ru"),
            ("Юркич", "Матвей", "Денисович", "yurkichmd23@vvsu.ithub.ru")
        ]

        for data in students_data:
            add_student(*data)

        db.session.commit()
        print("База данных успешно заполнена!")

if __name__ == '__main__':
    populate_database()