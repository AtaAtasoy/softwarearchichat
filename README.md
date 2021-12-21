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
python3 manage.py runserver
```
