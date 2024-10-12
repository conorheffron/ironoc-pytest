# ironoc-pytest

## Technologies: 
- pip, python 3.11, pytest, requests, pandas, & json

## Package Usage
### Install package
```shell
python3 -m pip install ironoc-pytest-conor-heffron
python3
```

### Usage Example:
```python
>>> import json
>>> from ironoc_pytest_conorheffron.github_api import GitHubClient
>>> gitHubClient = GitHubClient('conorheffron')
>>> result = gitHubClient.main()
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
>>> 
>>> gitHubClientDjango = GitHubClient('django')
>>> resultDjango = gitHubClientDjango.main()
>>> print(json.dumps(resultDjango, sort_keys=True, indent=4))
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

## Run Steps for Project Build & Tests Run:
```shell
# set environment
python3 -m venv pytest-env
source pytest-env/bin/activate

# install libraries
pip install -r requirements.txt

# Run tests and show standard out messages
pytest -s
```

## Run pytest from project Root Directory:
```shell
(pytest-env) ironoc-pytest % pytest
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.11.6, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/conorheffron/workspace/ironoc-pytest
configfile: pyproject.toml
collected 3 items                                                                                                                         

tests/test_github_api.py ...                                                                                                        [100%]

============================================================ 3 passed in 2.55s ============================================================
```
