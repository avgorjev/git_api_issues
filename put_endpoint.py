import requests
from base_endpoint import headers
from get_endpoint import url_id
import allure

payload_lock = {
    "lock_reason": "resolved"
}
url_id_lock = f"{url_id}/lock"


class LockingIssue:

    @allure.step('Locking an issue')
    def lock_issue(self):
        self.response = requests.request("PUT", url_id_lock, headers=headers, json=payload_lock)
        return self.response