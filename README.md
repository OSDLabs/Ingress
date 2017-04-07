# Ingress
A Portal for BITS

### Installation

If you are new to github, follow [git-task](https://github.com/OSDLabs/git-task) repository for basic knowledge on how to contribute.

* Make a fork of this repository on your account.

* Assuming you have python 3.4 already installed, go to the desired folder on your machine and follow these commands to clone the repository and install dependencies in a virtual environment:

```
$ virtualenv ingress
$ cd ingress
$ source bin/activate
$ git clone https://github.com/<USERNAME>/ingress src
$ cd src
$ pip3 install -r requirements.txt
```
NOTE for windows in the 3rd line use:
```
$ ingress\Scripts\activate
```

* db.sqlite3 is the database for this repository, you can delete that if you want to start with a fresh database and follow: (But not required and can skip this step)

```
$ touch ingress/credentials.py
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

* Create a superuser for admin controls (accessible at localhost:8000/admin)

```
$ python3 manage.py createsuperuser
```

* Run the server and access at localhost:8000

```
$ python3 manage.py runserver
```
## Application info
### Infographics
What is it?

**Displays various information and analyzes the course structure/syllabus etc. of our institute**

To setup:

* In the console (to extract information) `python3 infographics/datamine.py`

* Visit the url `/infographics/setup` to save data to the db

### Cab
What is it?

**A cab sharing app**
