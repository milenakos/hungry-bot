FROM python:3.15-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# The bot connects out to Discord and listens on no port. HUNGRY_TOKEN comes from the environment.
CMD ["python", "hungry.py"]
