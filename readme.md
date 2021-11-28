# Course Registration
- Website to allow students to register/unregister for courses 
- Features
	- Authentication
	- Displays all courses available along with details 
	- Students can choose the courses they want to register for 
	- Only admin can add,update or delete courses 
	- Student allowed to register for a course only when
        - Seats available in the particular course
        - Student has completed all the required prerequisite courses in the past
        - There is no time of day clash with any of the other registered courses
    - Schedule displayed in a calendar format for convenience
    - List of registered courses maintained for easy access by the student.
    
- Tech Stack   
	- HTML, CSS, JS for frontend
        - vanilla js for rendering some basic changes to frontend
        - ajax for sending/receiving post requests/responses to/from backend
        - CSS : Bootstrap and custom
    - Python, Django For backend development
        - views for defining controllers, helper and database functions
        - models to communicate with database 
    - SQLite Database
    - Deployment 
        - Deployed as an Application on heroku PAAS

## Usage

- Link to website
    https://student-course-registration.herokuapp.com/

- To Run locally
    - clone the repo 
        - ` git clone https://github.com/mohitgaggar/Course_Registration_Website.git`
    - Install requirements 
        - `pip install -r requirements.txt`
        (adviced to use a virtual environment)
    - go into the cloned repo and run the command
        - `python3 manage.py runserver`
    - go to http://127.0.0.1:8000/ to view the website


## Directory Structure


- Basic Tree structure (level 1 expansion)
.
├── Procfile 
├── course_registration_project     (Django Project name)
├── db.sqlite3      (Database)
├── home        ( Django app , handles authentication and the homepage)
├── manage.py
├── pick_courses        ( Django app to handle course selection and other course related features)
├── readme.md
├── requirements.txt
├── static
└── templates   (All html files)


- Structure With links
.
 * [course_registration_project](./course_registration_project)
   * [__init__.py](./course_registration_project/__init__.py)
   * [asgi.py](./course_registration_project/asgi.py)
   * [urls.py](./course_registration_project/urls.py)
   * [wsgi.py](./course_registration_project/wsgi.py)
   * [__pycache__](./course_registration_project/__pycache__)
   * [settings.py](./course_registration_project/settings.py)
 * [home](./home)
   * [__init__.py](./home/__init__.py)
   * [apps.py](./home/apps.py)
   * [tests.py](./home/tests.py)
   * [urls.py](./home/urls.py)
   * [admin.py](./home/admin.py)
   * [models.py](./home/models.py)
   * [migrations](./home/migrations)
   * [views.py](./home/views.py)
   * [__pycache__](./home/__pycache__)
   
 * [manage.py](./manage.py)
 * [pick_courses](./pick_courses)
   * [__init__.py](./pick_courses/__init__.py)
   * [apps.py](./pick_courses/apps.py)
   * [tests.py](./pick_courses/tests.py)
   * [urls.py](./pick_courses/urls.py)
   * [admin.py](./pick_courses/admin.py)
   * [models.py](./pick_courses/models.py)
   * [migrations](./pick_courses/migrations)
   * [views.py](./pick_courses/views.py)
   * [__pycache__](./pick_courses/__pycache__)
 * [venv1](./venv1)
 * [Procfile](./Procfile)
 * [templates](./templates)
   * [admin.html](./templates/admin.html)
   * [base.html](./templates/base.html)
   * [not_found.html](./templates/not_found.html)
   * [signin.html](./templates/signin.html)
   * [delete_course.html](./templates/delete_course.html)
   * [update_course.html](./templates/update_course.html)
   * [signup.html](./templates/signup.html)
   * [add_courses.html](./templates/add_courses.html)
   * [courses.html](./templates/courses.html)
   * [index.html](./templates/index.html)
 * [static](./static)
 * [requirements.txt](./requirements.txt)
 * [db.sqlite3](./db.sqlite3)
 * [readme.md](./readme.md)







.
├── Procfile
├── course_registration_project
├── db.sqlite3
├── file
├── home
├── manage.py
├── pick_courses
├── readme.md
├── requirements.txt
├── static
├── templates
└── venv1

6 directories, 6 files
