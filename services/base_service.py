import json
import requests


class BaseService:
    def post(self, url, body):
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.post(url, data=payload, headers=headers)
        return response.status_code, response.json()


    def get(self, url):
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return response.status_code, response.json()


    def put(self, url, body):
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.post(url, data=payload, headers=headers)
        return response.status_code, response.json()


    def delete(self, url):
        headers = {
            'accept': 'application/json'
        }
        response = requests.delete(url, headers=headers)
        return response.status_code, response.json()