# view/userview.py

from controller.usercontroller import UserController

class UserView:
    def __init__(self):
        self.controller = UserController()

    def exibir_interface(self):
        print("== Criar novo usuário ==")
        username = input("Digite o nome de usuário: ")
        email = input("Digite o email: ")
        self.controller.create_user(username, email)

        print("\n== Informações do usuário ==")
        print(self.controller.get_user_info())

        print("\n== Atualizar email ==")
        new_email = input("Digite o novo email: ")
        print(self.controller.change_user_email(new_email))

        print("\n== Informações atualizadas ==")
        print(self.controller.get_user_info())
