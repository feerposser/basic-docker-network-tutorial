FROM python:3

RUN mkdir /opt/exemplo

WORKDIR /opt/exemplo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD python app.py