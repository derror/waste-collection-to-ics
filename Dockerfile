FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Because of port 5000 is reserved by OSX
EXPOSE 5100

CMD [ "python", "app.py" ]
