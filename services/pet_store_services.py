import allure
from services.base_service import BaseService


class PetStoreServices(BaseService):
    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/store/order'

    @allure.step('Add place an order')
    def add_place_an_order(self, id_order, id_pet, quantity):
        body = {
            "id": id_order,
            "petId": id_pet,
            "quantity": quantity,
            "shipDate": "2024-09-30T13:11:02.580Z",
            "status": "placed",
            "complete": 'true'
        }
        url = self.url
        return self.post(url=url, body=body)

    @allure.step('Get pet by id')
    def get_pet_by_id(self, id_pet):
        url = f'{self.url}/{id_pet}'
        return self.get(url=url)

    @allure.step('Delete pet')
    def delete_pet(self, id_pet):
        url = f'{self.url}/{id_pet}'
        return self.delete(url=url)
