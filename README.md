# ironoc-pytest

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python package](https://github.com/conorheffron/ironoc-pytest/actions/workflows/python-package.yml/badge.svg)](https://github.com/conorheffron/ironoc-pytest/actions/workflows/python-package.yml)

[![Upload Python Package](https://github.com/conorheffron/ironoc-pytest/actions/workflows/python-publish.yml/badge.svg)](https://github.com/conorheffron/ironoc-pytest/actions/workflows/python-publish.yml)

## Package URL
- [https://pypi.org/p/ironoc-pytest-conor-heffron/](https://pypi.org/p/ironoc-pytest-conor-heffron/)

## Technologies: 
- pip3, python 3.14, pytest, requests, pandas, & json

## Run Steps for Project Build & Tests Run:
```shell
# set environment
python3 -m venv pytest-env
source pytest-env/bin/activate

# install libraries
pip3 install -r requirements.txt

# Run tests and show standard out messages
pytest -s
```

## Run pytest from project Root Directory:
```shell
(pytest-env) ironoc-pytest % pytest
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.14.0, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/conorheffron/workspace/ironoc-pytest
configfile: pyproject.toml
collected 3 items                                                                                                                                                                                                          

src/ironoc_pytest_conorheffron/tests/test_github_api.py ...                                                                                                                                                          [100%]

==================================================================================================== 3 passed in 1.05s =====================================================================================================
```

## Standalone `PyPi` Package Usage
### Install package & Set Environment
```shell
python3 -m pip install ironoc-pytest-conor-heffron
python3 -m venv pytest-env
source pytest-env/bin/activate
python3
```

### Usage Examples & Run Packages Tests:
 - #### Run client call for user `conorheffron`
```python
>>> import json
>>> from ironoc_pytest_conorheffron.github_api import GitHubClient
>>> git_hub_client = GitHubClient('conorheffron')
>>> result = git_hub_client.main()
>>> print(json.dumps(result, sort_keys=True, indent=4))
{
    "1": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/bio-cell-red-edge\"}",
    "2": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/booking-sys\"}",
    "3": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/cbio-skin-canc\"}",
    "4": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/conorheffron\"}",
    "5": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/cron-job-sample\"}",
    "6": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/elastic-tester\"}",
    "7": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/fun-with-r\"}",
    "8": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/gene-expr\"}",
    "9": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/global-max-sim-matrix\"}",
    "10": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/graphql-box\"}",
    "11": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc\"}",
    "12": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-db\"}",
    "13": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-msg\"}",
    "14": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-pytest\"}",
    "15": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-spark\"}",
    "16": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/kdb-bots\"}",
    "17": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/kdb-tick\"}",
    "18": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/marjaderoniet\"}",
    "19": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/mern-essential-training\"}",
    "20": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/mern-sandbox\"}",
    "21": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/nba-stats\"}",
    "22": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/netflix-movie-duration\"}",
    "23": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/normalise-fetalh\"}",
    "24": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/normalise-spotify\"}",
    "25": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/nyc-school-scores\"}",
    "26": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/python-sandbox\"}",
    "27": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/rabbitmq-tester\"}",
    "28": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/react-graphql-course\"}",
    "29": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/redis-tester\"}",
    "30": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ronoc-packages\"}",
    "31": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/scala-course\"}",
    "32": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/skills-publish-packages\"}"
}
```

 - #### Run client call for organisation `django`
```python
>>> git_client_django = GitHubClient('django')
>>> result_django = git_client_django.main()
>>> print(json.dumps(result_django, sort_keys=True, indent=4))
{
    "1": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/.github\"}",
    "2": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/asgiref\"}",
    "3": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/asgi_ipc\"}",
    "4": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/channels\"}",
    "5": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/channels_redis\"}",
    "6": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/code-of-conduct\"}",
    "7": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/code.djangoproject.com\"}",
    "8": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/daphne\"}",
    "9": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/deps\"}",
    "10": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django\"}",
    "11": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-asv\"}",
    "12": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-box\"}",
    "13": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-contrib-comments\"}",
    "14": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-docker-box\"}",
    "15": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-docs-translations\"}",
    "16": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-fuzzers\"}",
    "17": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/django-localflavor\"}",
    "18": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/djangobench\"}",
    "19": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/djangopeople\"}",
    "20": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/djangoproject.com\"}",
    "21": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/djangosnippets.org\"}",
    "22": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/dsf-working-groups\"}",
    "23": "{\"login\": \"django\", \"id\": 27804, \"url\": \"https://github.com/django/ticketbot\"}"
}
```

 - #### Run all package tests
```python
>>> import pytest
>>> pytest.main(['--pyargs',  'ironoc_pytest_conorheffron.tests', '-s'])
==================================================================================== test session starts ====================================================================================
...
collected 3 items                                                                                                                                                                           

pytest-env/lib/python3.11/site-packages/ironoc_pytest_conorheffron/tests/test_github_api.py {
    "1": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/bio-cell-red-edge\"}",
    "2": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/booking-sys\"}",
    "3": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/cbio-skin-canc\"}",
    "4": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/conorheffron\"}",
    "5": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/cron-job-sample\"}",
    "6": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/elastic-tester\"}",
    "7": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/fun-with-r\"}",
    "8": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/gene-expr\"}",
    "9": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/global-max-sim-matrix\"}",
    "10": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/graphql-box\"}",
    "11": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc\"}",
    "12": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-db\"}",
    "13": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-msg\"}",
    "14": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-pytest\"}",
    "15": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ironoc-spark\"}",
    "16": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/kdb-bots\"}",
    "17": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/kdb-tick\"}",
    "18": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/marjaderoniet\"}",
    "19": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/mern-essential-training\"}",
    "20": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/mern-sandbox\"}",
    "21": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/nba-stats\"}",
    "22": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/netflix-movie-duration\"}",
    "23": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/normalise-fetalh\"}",
    "24": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/normalise-spotify\"}",
    "25": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/nyc-school-scores\"}",
    "26": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/python-sandbox\"}",
    "27": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/rabbitmq-tester\"}",
    "28": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/react-graphql-course\"}",
    "29": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/redis-tester\"}",
    "30": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/ronoc-packages\"}",
    "31": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/scala-course\"}",
    "32": "{\"login\": \"conorheffron\", \"id\": 8218626, \"url\": \"https://github.com/conorheffron/skills-publish-packages\"}"
}
.{
    "1": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/alfred-calendly\"}",
    "2": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/alfred-devdocs\"}",
    "3": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/alfred-jq\"}",
    "4": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/alfred-linkify\"}",
    "5": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/alfred-time-since\"}",
    "6": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/algorithms\"}",
    "7": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/docs\"}",
    "8": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/meta\"}",
    "9": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/notebooks\"}",
    "10": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/notion-search-alfred-workflow\"}",
    "11": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/sgpt\"}",
    "12": "{\"login\": \"meta\", \"id\": 5732757, \"url\": \"https://github.com/meta/the-book-of-secret-knowledge\"}"
}
.{
    "1": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/alert-notification-helloworld\"}",
    "2": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/ansible-collection-ibm\"}",
    "3": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/ansible-ibm-docs\"}",
    "4": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/ansible.ibm.cloud\"}",
    "5": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/appid-samples\"}",
    "6": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/application-log-analysis\"}",
    "7": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/arch-hybrid-data-carcare\"}",
    "8": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/architecture-icons\"}",
    "9": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/argo-events\"}",
    "10": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/aspnet-core-cloudant\"}",
    "11": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/aspnet-core-helloworld\"}",
    "12": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/aspnet-core-todo\"}",
    "13": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/assistant-shop.r\"}",
    "14": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/auto-scaling-demo\"}",
    "15": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bare-metal-enablement-demo\"}",
    "16": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/big-data-log-analytics\"}",
    "17": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/BigInsights-on-Apache-Hadoop\"}",
    "18": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/blast-radius\"}",
    "19": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluechatter\"}",
    "20": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-car-rally-charge-coupon\"}",
    "21": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-cloud-connectors\"}",
    "22": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/Bluemix-ContextPathRouting\"}",
    "23": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-go\"}",
    "24": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-hello-iojs-container\"}",
    "25": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-hr-outreach\"}",
    "26": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/Bluemix-onprem-data\"}",
    "27": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-retail\"}",
    "28": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/Bluemix-ServiceBroker\"}",
    "29": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-ti-board-starter\"}",
    "30": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluemix-workshops\"}",
    "31": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bluetag\"}",
    "32": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/bms-samples-ios-helloworld\"}",
    "33": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/box-watson\"}",
    "34": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/capital-weather\"}",
    "35": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/car-data-management\"}",
    "36": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cdn-with-cda-todolist\"}",
    "37": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-client-electron\"}",
    "38": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-client-java\"}",
    "39": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-client-node\"}",
    "40": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-client-python\"}",
    "41": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-client-swift\"}",
    "42": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-deployment-tracker-service\"}",
    "43": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-fed-wiki\"}",
    "44": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-log-slack\"}",
    "45": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-manifest-generator\"}",
    "46": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-models\"}",
    "47": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-nodejs-c2c-demo\"}",
    "48": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf-nodejs-client\"}",
    "49": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cfee-eirini-storefront\"}",
    "50": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cfee-service-broker-kubernetes\"}",
    "51": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cf_deployment_tracker_client_go\"}",
    "52": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/chatbot-watson-android\"}",
    "53": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/client-go\"}",
    "54": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-button\"}",
    "55": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-event-management-sample\"}",
    "56": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-journey\"}",
    "57": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-provider-ibm\"}",
    "58": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-provider-vpc-controller\"}",
    "59": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloud-sql-database\"}",
    "60": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloudco-insurance\"}",
    "61": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/clouddatabases-helloworld-examples\"}",
    "62": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/clouddatabases-helloworld-kubernetes-examples\"}",
    "63": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/clouddatabases-migration-examples\"}",
    "64": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/clouddatabases-redis-helloworld-python\"}",
    "65": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/CloudFoundry-to-CodeEngine\"}",
    "66": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cloudmailer\"}",
    "67": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/code-engine-text-analysis\"}",
    "68": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/codeback\"}",
    "69": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/codeignitor-db\"}",
    "70": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/collaboration\"}",
    "71": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/community.ansible.ibm.cloud\"}",
    "72": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-elasticsearch-helloworld-nodejs\"}",
    "73": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-etcd-helloworld-nodejs\"}",
    "74": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-mongodb-helloworld-nodejs\"}",
    "75": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-mysql-helloworld-nodejs\"}",
    "76": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-postgresql-helloworld-nodejs\"}",
    "77": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-rabbitmq-helloworld-nodejs\"}",
    "78": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-redis-helloworld-nodejs\"}",
    "79": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-rethinkdb-helloworld-nodejs\"}",
    "80": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/compose-scylladb-helloworld-nodejs\"}",
    "81": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/concept-insights-eclipse-faq\"}",
    "82": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/configuration-discovery\"}",
    "83": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/connections\"}",
    "84": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/container-registry-builder\"}",
    "85": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/container-services-go-sdk\"}",
    "86": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/controller-kinect-bluemix\"}",
    "87": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/cross-account-resource-sharing\"}",
    "88": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/CRUD-PHP-Codeigniter-Bluemix\"}",
    "89": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/dashdb-nodejs-helloworld\"}",
    "90": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/data\"}",
    "91": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/data-lake\"}",
    "92": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/data-store-for-memcache-client\"}",
    "93": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/db-benchmark\"}",
    "94": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/DevOps-Services-Docs\"}",
    "95": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/django-boilerplate\"}",
    "96": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/docker-node-xvfb\"}",
    "97": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/docplexcloud-helloworld-nodejs\"}",
    "98": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/docs\"}",
    "99": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/docs-services\"}",
    "100": "{\"login\": \"IBM-Cloud\", \"id\": 7284885, \"url\": \"https://github.com/IBM-Cloud/doctor-watson\"}"
}
.

===================================================================================== 3 passed in 0.54s =====================================================================================
```
