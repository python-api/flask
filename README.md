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

### Run program

```shell
flask --app hello run

# Externally Visible Server
flask --app hello run --host=0.0.0.0

# To enable debug mode, use the --debug option.
flask --app hello run --host=0.0.0.0 --debug
```

# Documentation

### [Python Documentation](https://docs.python.org)

### [Flask](https://palletsprojects.com/p/flask/)

### [FastAPI](https://fastapi.tiangolo.com/)