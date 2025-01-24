FROM python:3.11-slim

WORKDIR /backend

COPY ./backend/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend /backend/

CMD ["fastapi", "run", "backend/main.py"]
