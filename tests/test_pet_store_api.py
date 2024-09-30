from services.pet_store_services import PetStoreServices


def test_add_place_an_order():
    pet_store = PetStoreServices()

    id_order = 777
    id_pet = 1000
    quantity = 3000

    status_code, response = pet_store.add_place_an_order(id_order, id_pet, quantity)

    assert status_code == 200
    assert response['id'] == id_order
    assert response['petId'] == id_pet
    assert response['quantity'] == quantity


def test_find_by_id():
    pet_store = PetStoreServices()

    status_code, response = pet_store.get_pet_by_id(777)

    assert status_code == 200
    assert response['id'] == 777


def test_delete_pet():
    pet_store = PetStoreServices()

    status_code, response = pet_store.delete_pet(777)

    assert status_code == 200
    assert response['code'] == 200
    assert response["type"] == "unknown"
    assert response["message"] == "777"
