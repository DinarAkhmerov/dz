class Users:
    age = 18
    first_name = ""
    last_name = ""

    def __init__(self, age=18, first_name="Name", last_name="Last name"):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def get_users(self):
        print(f"Имя: {self.first_name}, Фамилия: {self.last_name}, Возраст: {self.age}")

    def __del__(self):
        print(f"Удаление экземпляра: {str(self)}")


elena = Users(17, "Елена", "Иванова")
elena.get_users()