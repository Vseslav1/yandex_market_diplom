import json
import requests
import allure
from helpers.logger import create_logger


class BaseService:
    def __init__(self):
        self.logger = create_logger()

    @allure.step('Method post')
    def post(self, url, body):
        self.logger.info(f'Executing POST request to {url} with body: {body}')
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.post(url, data=payload, headers=headers)
        self.logger.info(f'POST response: {response.status_code} - {response.json()}')
        return response.status_code, response.json()

    @allure.step('Method get')
    def get(self, url):
        self.logger.info(f'Executing GET request to {url}')
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        self.logger.info(f'GET response: {response.status_code} - {response.json()}')
        return response.status_code, response.json()

    @allure.step('Method put')
    def put(self, url, body):
        self.logger.info(f'Executing PUT request to {url} with body: {body}')
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.put(url, data=payload, headers=headers)
        self.logger.info(f'PUT response: {response.status_code} - {response.json()}')
        return response.status_code, response.json()

    @allure.step('Method delete')
    def delete(self, url):
        self.logger.info(f'Executing DELETE request to {url}')
        headers = {
            'accept': 'application/json'
        }
        response = requests.delete(url, headers=headers)
        self.logger.info(f'DELETE response: {response.status_code} - {response.json()}')
        return response.status_code, response.json()