import allure
from services.pet_service import PetService


@allure.title('Test add pet')
def test_add_pet():
    pet = PetService()

    id_pet = 222
    name = 'Sharic'

    status_code, response = pet.add_pet(id_pet, name)
    assert status_code == 200
    assert response['id'] == 222
    assert response['name'] == 'Sharic'


@allure.title('Test update pet')
def test_update_pet():
    pet = PetService()

    pet.update_pet(222, 'Bobik', 'sale')

    status_code, response = pet.get_pet_by_id(222)

    assert status_code == 200
    assert response['name'] == 'Bobik'
    assert response['status'] == 'sale'


@allure.title('Test get pet')
def test_get_pet():
    pet = PetService()

    status_code, response = pet.get_pet_by_id(222)

    assert status_code == 200
    assert response['id'] == 222
    assert response['name'] == 'Bobik'
    assert response['status'] == 'sale'


@allure.title('Test delete pet')
def test_delete_pet():
    pet = PetService()

    status_code, response = pet.del_pet(222)

    assert status_code == 200
    assert response['code'] == 200
    assert response["type"] == "unknown"
    assert response["message"] == "222"
