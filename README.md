# SoftwareArchichat

## Group Members

* Hüseyin Ata Atasoy
* Mehmet Ali Altunsoy

## Instructions to run the program

Docker is required to run the program.

```bash
python3 -m venv venv
(bash/zsh) source venv/bin/activate  # For POSIX platforms
(CMD) <venv>\Scripts\activate.bat # For Windows
(PS) C:\> <venv>\Scripts\Activate.ps1 # For Windows PowerShell
pip install -r requirements.txt
docker run -p 6379:6379 -d redis:5
cd myapp
python3 manage.py runserver
```

## Code Structure

* The code for the program is under `myapp/`
* `static` contains the logos, css files and the Javascript files.
* `accountmanager` is its own app that is responsible for managing user accounts, obviously.
* `chat` is its own app and it contains the chatting logic of the project.
* `templates` directory under `accountmanager` and `chat` contains the Django Templates (UI).
* `views.py` files manage the rendering process for `accountmanager` and `chat` apps.
* `models.py` under `chat/` contain the data models used in the app.
* `urls.py` file contains the URL configurations for the applications.
* `settings.py` under `myapp/` is used for django project settings.
