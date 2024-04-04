FROM python:3.9.12-alpine3.15
# Default Flask port
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
CMD [ "python",  "app.py" ]
