FROM python
RUN apt-get update && apt-get install python3-pip -y && apt-get install python-dev -y
WORKDIR /projetoFlask
COPY .env app.py database.py models.py routes.py settings.py requirements.txt /projetoFlask/
WORKDIR /projetoFlask
RUN pip install -r requirements.txt 
RUN pip install flask
CMD ["python","app.py"]