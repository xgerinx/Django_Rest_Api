This program create API endpoints
(Python, Django, Django Rest Framework)

You need Docker to run this project.
Use "python manage.py loaddata fixtures/main.json" command to fill databace with data

1. /courses/ <-- Link to list of all courses
2. /courses/1/ <-- This is rout to course with id - 1 (enter your number for different result)
3. /courses/1/price/ <-- Here you can find price of the course by id - 1
4. /sections/ <-- Same as courses but for sections
5. /sections/1/ <-- Same as courses but for sections
6. /courses/with-sections/ <-- This link show list of all courses and all sections attach to this courses