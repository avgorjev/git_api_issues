from base_endpoint import url, headers
import requests
import allure


payload_get = {}

class ListingIssue:

    @allure.step('Generating an issues report')
    def list_created_issues(self):
        self.response = requests.request("GET", url, headers=headers, json=payload_get)
        return self.response


class GettingIssue:

    @allure.step('Opening an issue')
    def check_issue(self, url_id):
        self.response = requests.request("GET", url_id, headers=headers, json=payload_get)
        return self.response


url_id = f"{url}/{ListingIssue().list_created_issues().json()[0]['number']}"