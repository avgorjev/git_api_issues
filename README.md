# Тестовые сценарии для [GitHub Issues](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#about-issues)

Запуск тестов: test_api_issue.py в разделе [Actions](https://github.com/avgorjev/git_api_issues/actions)


```
name:
  Tests for REST API endpoints for issues

on:
  push

jobs:
  test:
    runs-on: macos-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install requirements
        run: pip install -r requirements.txt
      - name: first_test
        run: pytest
```
