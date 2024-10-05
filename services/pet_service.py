import allure
from services.base_service import BaseService


class PetService(BaseService):

    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/pet'

    @allure.step('Add pet')
    def add_pet(self, id_pet, name):
        body = {
              "id": id_pet,
              "category": {
                "id": 0,
                "name": "string"
              },
              "name": name,
              "photoUrls": [
                "string"
              ],
              "tags": [
                {
                  "id": 0,
                  "name": "string"
                }
              ],
              "status": "available"
            }
        url = self.url
        return self.post(url=url, body=body)

    @allure.step('Get pet by id')
    def get_pet_by_id(self, id_pet):
        url = f'{self.url}/{id_pet}'
        return self.get(url=url)

    @allure.step('Update pet')
    def update_pet(self, id_pet, name, status):
        body = {
            "id": id_pet,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": status
        }
        url = self.url
        return self.put(url=url, body=body)

    @allure.step('Delete pet')
    def del_pet(self, id_pet):
        url = f'{self.url}/{id_pet}'
        return self.delete(url=url)