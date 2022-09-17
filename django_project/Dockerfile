From python:3
RUN pip install django

COPY . .

RUN python manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]


