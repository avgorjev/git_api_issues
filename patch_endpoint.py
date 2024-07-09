import allure
import requests
from base_endpoint import headers
from get_endpoint import url_id
import allure


payload_patch = {
  "body": "Я нашел новый баг"
}


class UpdatingIssue:

    @allure.step('Editing an issue')
    def update_issue(self):
        self.response = requests.request("PATCH", url_id, headers=headers, json=payload_patch)
        return self.response
