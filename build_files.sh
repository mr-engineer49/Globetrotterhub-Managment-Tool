# build_files.sh
source venv/Scripts/activate pip install -r requirements.txt
source venv/Scripts/activate python3.9 manage.py collectstatic