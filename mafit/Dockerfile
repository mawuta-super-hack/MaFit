FROM python:3.10-slim 

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY  . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mafit.wsgi"] 