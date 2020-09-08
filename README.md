## A Platform for Online Education 

###### *The backend is built using REST API principles*

**Installation**

Copy a the repository on your local machine and install dependencies

```
$ git clone https://github.com/ImagineImogen/onlinecourses.git
$ pip install -r requirements.txt
```

Run server


```
$ python manage.py runserver
```

## To run inside a Docker container

start:
```
$ docker-compose up -d --build --remove-orphans
```
restart:
```
$ docker-compose stop && docker-compose up -d --build --remove-orphans
```
stop:
```
$ docker-compose stop
```
down:
```
$ docker-compose down -v
```

**API Endpoints include:**

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

[http://127.0.0.1:8000/api/1](http://127.0.0.1:8000/api/1)

[http://127.0.0.1:8000/api/lessons/1](http://127.0.0.1:8000/lessons/1)

[http://127.0.0.1:8000/api/users/register](http://127.0.0.1:8000/users/register)

[http://127.0.0.1:8000/api/users/login](http://127.0.0.1:8000/users/login/)


[http://127.0.0.1:8000/api/users/logout](http://127.0.0.1:8000/users/logout/)


#### Example API response

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "Potion-Making - Beginner's course",
        "description": "This highly-rated online course will guide you step-by-step through the composition of your first potion and other related aspects of potion-making",
        "lessons": [
            {
                "id": 1,
                "title": "Induction - What is a potion making?",
                "description": "What is a potion making and what will you need during our course?",
                "course": "Potion-Making - Beginner's course"
            }
        ],
        "teacher": [
            {
                "teacher_name": "Roman Oculus"
            }
        ]
    },
    {
        "id": 2,
        "title": "Spells - From Zero to Hero",
        "description": "An all-comprising course suitable for the people who just took their wands for the first time. Be ready for the fascinating journey into the witchcraft world featuring the most commonly used spells to make your life much easy!",
        "lessons": [],
        "teacher": []
    },
    {
        "id": 3,
        "title": "Magical Beasts - Introductory course",
        "description": "Step into the marvellous world of powerful creatures and avoid being killed!",
        "lessons": [],
        "teacher": []
    }
]

```



## License
[MIT](https://choosealicense.com/licenses/mit/)