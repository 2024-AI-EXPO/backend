FROM python:3.9

WORKDIR /symbols_backend

COPY requirements.txt /symbols_backend/requirements.txt

RUN pip install --no-cache-dir -r /symbols_backend/requirements.txt

COPY ./src /symbols_backend/src
COPY ./main.py /symbols_backend/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
