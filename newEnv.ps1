# Setup d'environement sur un nouveau PC
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt