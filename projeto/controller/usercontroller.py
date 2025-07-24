# controller/usercontroller.py

from model.user import User

class UserController:
    def __init__(self):
        self.user = None

    def create_user(self, username, email):
        self.user = User(username, email)

    def get_user_info(self):
        if self.user:
            return self.user.get_info()
        return "Nenhum usuário criado."

    def change_user_email(self, new_email):
        if self.user:
            self.user.update_email(new_email)
            return "Email atualizado com sucesso."
        return "Nenhum usuário para atualizar."
