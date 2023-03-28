<p align="center">
<a href="/" target="_blank">
<img src="logo.svg" width="400" alt="Logo">
</a></p>

___

## Git Repositories

- [GitHub](https://github.com/python-api/flask)
- [GitLab](https://gitlab.com/hainghia/flask)
- [Bitbucket](https://bitbucket.org/hainghia/flask)

### Remote repository

```shell
git remote -v

git remote add origin git@github.com:python-api/flask.git
git remote add gitlab git@gitlab.com:hainghia/flask.git
git remote add bitbucket git@bitbucket.org:hainghia/flask.git


git add .; git commit -asm "Initial commit";git push origin main; git push gitlab main; git push bitbucket main
```

## Install python and Pip (PowerShell administrator)

```shell
choco install python
py -m pip install --upgrade pip
```

## [Package Manager pypi](https://pypi.org/)

```shell
# Will produce a similar list of the installed packages
pip freeze > requirements.txt

# Users can then install all the necessary packages
pip install -r requirements.txt
```

## How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 20.04

```shell
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv

python3 -m venv venv
```

```shell
py -m venv venv

# Activate the environment
venv\Scripts\activate
source venv/bin/activate

pip install Flask

# Deactivate the environment
deactivate
```

Check version Flask

```shell
flask --version
```

### Run program

```shell
py app.py

```

```shell
flask --app app init-db
flask --app app run --host=0.0.0.0 --port=80 --debug --reload

pytest
pytest -v
coverage run -m pytest
coverage report
coverage html


```

# Documentation

### [Python Documentation](https://docs.python.org)

### [Flask](https://palletsprojects.com/p/flask/)

### [FastAPI](https://fastapi.tiangolo.com/)

# [Project layout](https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/)

```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```
___

### [Apache Kafka](https://kafka.apache.org/quickstart)

```shell
start https://www.apache.org/dyn/closer.cgi?path=/kafka/3.4.0/kafka_2.13-3.4.0.tgz
```

# Docker

```shell
docker kill $(docker ps -aq); docker rm $(docker ps -aq); docker rmi $(docker images -aq); docker volume prune -f;

make stop-user-development; make build-user-development; make start-user-development
make stop-user-production; make build-user-production; make start-user-production
```

https://docs.docker.com/samples/flask/
https://www.sqlalchemy.org/