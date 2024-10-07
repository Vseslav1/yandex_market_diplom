import allure
from services.user_services import UserServices


@allure.title('Add user')
def test_add_user():
    user_services = UserServices()

    id_user = 444
    username = 'TeachMeSkill'
    first_name = 'Alex'
    last_name = 'Ivanov'
    email = 'alex1234@gmai.com'
    password = '1234'
    phone = '11223344'
    user_status = 1

    status_code, response = user_services.create_user(id_user, username, first_name, last_name, email, password, phone,
                                                      user_status)

    assert status_code == 200


@allure.title('Test get user by user name')
def test_get_user_by_user_name():
    user_services = UserServices()

    status_code, response = user_services.get_user_by_username('TeachMeSkill')

    assert status_code == 200
    assert response['id'] == 444
    assert response['username'] == 'TeachMeSkill'
    assert response['firstName'] == "Alex"
    assert response['lastName'] == "Ivanov"
    assert response['email'] == "alex1234@gmai.com"
    assert response['password'] == "1234"
    assert response['phone'] == "11223344"
    assert response['userStatus'] == 1


@allure.title('Test login user')
def test_login_user():
    user_services = UserServices()

    status_code, response = user_services.login_user('TeachMeSkill', "1234")

    assert status_code == 200
