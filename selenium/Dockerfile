FROM joyzoursky/python-chromedriver:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "selenium_docker.py"]