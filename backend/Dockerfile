FROM python:3.11-slim

WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["fastapi", "run", "main.py"]
