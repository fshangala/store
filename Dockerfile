# base image  
FROM python:3.10 

WORKDIR /app

COPY . . 
 
RUN pip install -r requirements.txt

EXPOSE 80

CMD python manage.py runserver