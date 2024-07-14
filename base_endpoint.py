import allure
import os
import requests


GITHUB_TOKEN = os.environ['github_token']
owner = "avgorjev"
repo = "git_api_issues"
url = f"https://api.github.com/repos/{owner}/{repo}/issues"
payload = {
      "title": "Issue 1",
      "body": "Я нашел баг",
      "assignees": [
        f"{owner}"
      ],
      "labels": [
        "bug"
      ]
}
headers = {
      'Accept': 'application/vnd.github+json',
      'Authorization': f'Bearer {GITHUB_TOKEN}',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
      'Cookie': '_octo=GH1.1.809836981.1720270408; logged_in=yes'
}


class Asserts:

    @allure.step('Checking the issue title')
    def check_title(self, response, title):
        assert response.json()['title'] == title

    @allure.step('Checking the issue body')
    def check_body(self, response, body):
        assert response.json()['body'] == body

    @allure.step('Checking the issue assignees')
    def check_assignees(self, response, assignee):
        assert response.json()['assignees'][0]['login'] == assignee

    @allure.step('Checking the issue labels')
    def check_labels(self, response, label):
        assert response.json()['labels'][0]['name'] == label

    @allure.step('Checking the status 200 OK')
    def check_status_is_200(self, response):
        assert response.status_code == 200

    @allure.step('Checking the status 201 Created')
    def check_status_is_201(self, response):
        assert response.status_code == 201

    @allure.step('Checking the status 204 No Content')
    def check_status_is_204(self, response):
        assert response.status_code == 204

    @allure.step('Checking the issue in the list')
    def check_issue_numbers(self, created_id, list_first_id):
        assert created_id == list_first_id
