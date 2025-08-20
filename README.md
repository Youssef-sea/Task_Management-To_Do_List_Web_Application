# Task_Management-To_Do_List_Web_Application
ALX Back-End Capstone 

Task Management Application
A simple web application for managing personal tasks, built as a capstone project for the ALX Backend Development program. This project demonstrates core backend skills in Python, Django, and SQL.

*Features
This is a summary of the features implemented so far:

	User Authentication: Secure user registration, login, and logout. Users can only access the application after logging in.

	Task Management:

		Create: Users can create new tasks with a title, description, and due date.

		Read: Users can view a list of all their tasks and see detailed information for a single task.

		Update: Users can edit existing tasks, including marking them as complete.

	Data Isolation: All tasks are tied to their specific user, ensuring that users can only view and manage their own data.

*Getting Started
Follow these steps to set up and run the project on your local machine.

*Prerequisites
	Python 3.x
	Git

Installation
	1-Clone the repository:

git clone https://github.com/Youssef-sea/Task_Management-To_Do_List_Web_Application.git
cd Task_Management-To_Do_List_Web_Application

	2-Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate  # For Windows

	3-Install project dependencies:

pip install -r requirements.txt


	4-Run database migrations:

python manage.py makemigrations
python manage.py migrate

	5-Create an admin superuser:

python manage.py createsuperuser


python manage.py createsuperuser --noinput --username <your_username> --email <your_email>
python manage.py shell
# In the Python shell, run:
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(username='<your_username>')
u.set_password('<your_password>')
u.save()

	6-Run the development server:

python manage.py runserver

The application will be available at http://127.0.0.1:8000/.

*Technologies Used
	Backend: Python
	Web Framework: Django
	Database: SQLite3 (for development)
	Operating System: Windows
	Version Control: Git & GitHub

*Future Plans
The project will continue to be developed based on the initial project plan. The next steps include:
	Implementing the task deletion functionality.
	Improving the user interface and styling of the templates.
	Adding more features like searching, filtering, and sorting tasks.