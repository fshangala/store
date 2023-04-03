# base image  
FROM python:3.10 

WORKDIR /app

COPY . . 
 
RUN pip install -r requirements.txt
RUN cp .env.dist .env

EXPOSE 80

CMD ["python","manage.py","runserver","0.0.0.0:80"]