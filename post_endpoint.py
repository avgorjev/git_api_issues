from base_endpoint import url, headers, payload
import requests
import allure

class CreatingIssue:

    @allure.step('Create new issue')
    def new_issue(self):
        self.response = requests.request("POST", url, headers=headers, json=payload)
        return self.response


    @allure.step('Number identification')
    def number_issue(self):
        self.response = requests.request("POST", url, headers=headers, json=payload).json()['number']
        return self.response
