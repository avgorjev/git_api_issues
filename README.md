# Тестовые сценарии для [GitHub Issues](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#about-issues)

Запуск тестов: test_api_issue.py в разделе [Actions](https://github.com/avgorjev/git_api_issues/actions)

![Tests for REST API endpoints for issues](https://github.com/avgorjev/git_api_issues/actions/workflows/run_api_tests.yml/badge.svg)


```
name:
  Tests for REST API endpoints for issues

on:
  workflow_dispatch

env:
  github_token: ${{ secrets.API_TOKEN }}

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  test:
    runs-on: ubuntu-latest
    name: running_tests

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: All tests (with pytest and allure)
      run: |
        pytest -v -s --alluredir reports
      continue-on-error: true  
    - name: Save results
      uses: actions/upload-artifact@v4
      with:
        name: reports
        path:
          reports
        retention-days: 1

  prepare_reports:

    runs-on: macos-latest
    needs: test
    name: creating_report

    steps:
      - uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '21'
      - run: brew install allure
      - name: Download artifact
        uses: actions/download-artifact@v4
      - run: allure generate -c reports -o _site
      - name: Save reports
        uses: actions/upload-artifact@v4
        with:
          name: _site
          path:
            _site
          retention-days: 1

  show_reports:

    runs-on: ubuntu-latest
    needs: prepare_reports
    name: screening_report

    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
