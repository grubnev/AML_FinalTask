FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Установка pytest
RUN pip install pytest

CMD ["streamlit", "run", "app.py"]
