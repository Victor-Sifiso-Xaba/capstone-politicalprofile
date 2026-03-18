# Capstone Political Profile

## Run locally
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python capstone/manage.py migrate
python capstone/manage.py runserver

## Run with Docker
docker build -t politicalprofile .
docker run -p 8000:8000 politicalprofile

Visit: http://127.0.0.1:8000/
