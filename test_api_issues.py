from base_endpoint import Asserts, payload
from get_endpoint import ListingIssue, GettingIssue, url_id
from patch_endpoint import UpdatingIssue, payload_patch
from put_endpoint import LockingIssue
from post_endpoint import CreatingIssue
import allure


post_issue = CreatingIssue()
list_issue = ListingIssue()
get_issue = GettingIssue()
patch_issue = UpdatingIssue()
put_issue = LockingIssue()
asserts = Asserts()


@allure.story('Create an issue')
@allure.feature('POST')
def test_create_issue():
    '''
    The issue was successfully generated
    '''
    response = post_issue.new_issue()
    asserts.check_title(response, payload['title'])
    asserts.check_body(response, payload['body'])
    asserts.check_assignees(response, payload['assignees'][0])
    asserts.check_labels(response, payload['labels'][0])
    asserts.check_status_is_201(response)


@allure.story('List repository issues')
@allure.feature('GET')
def test_check_list_issue():
    '''
    The created issue is in the list
    '''
    asserts.check_issue_numbers(post_issue.number_issue(), list_issue.list_created_issues().json()[0]['number'])


@allure.story('Get an issue')
@allure.feature('GET')
def test_get_issue():
    response = get_issue.check_issue(url_id)
    asserts.check_status_is_200(response)


@allure.story('Update an issue')
@allure.feature('PATCH')
def test_update_issue():
    '''
    Changing the contents of the body field
    '''
    response = patch_issue.update_issue()
    asserts.check_status_is_200(response)
    asserts.check_body(response, payload_patch['body'])


@allure.story('Lock an issue')
@allure.feature('PUT')
def test_lock_issue():
    '''
    Switching the issue to completed status due to resolved
    '''
    response = put_issue.lock_issue
    asserts.check_status_is_204(response)
