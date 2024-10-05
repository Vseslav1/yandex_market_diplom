import allure
from services.base_service import BaseService


class UserServices (BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/user'

    @allure.step('Method get')
    def create_user(self, id_user, user_name, first_name, last_name, email, password, phone, user_status):
        body = {
            "id": id_user,
            "username": user_name,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": user_status
        }
        url = self.url
        return self.post(url=url, body=body)

    @allure.step('Get user by user name')
    def get_user_by_username(self, user_name):
        url = f'{self.url}/{user_name}'
        return self.get(url=url)

    @allure.step('Login user')
    def login_user(self, username, password):
        url = f'{self.url}/login?username={username}&password={password}'
        return self.get(url=url)
