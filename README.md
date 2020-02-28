mjuseoul.likelion.org
===

📖 Introduction
---
This project is a site for applying Likelion at MJU Seoul

🏁 Start
---
first of all, prepare a virtual environment with the django and several packages

### 1. create virtual environment
```bash
$ python -m venv venv
```
The name of virtual environment is defined by "venv"

### 2. activate virtual environment
```bash
$ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux
```

### 3. install pip packages
```bash
$ pip install -r requirements.txt
```
The required packages are defined in the requirements.txt file.

If additional packages are installed, the following commands should be executed.

```bash
$ pip freeze > requirements.txt
```

🧐 What's inside?
---
    .
    ├── config
    ├── page
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt

