# user.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}"

    def update_email(self, new_email):
        self.email = new_email
