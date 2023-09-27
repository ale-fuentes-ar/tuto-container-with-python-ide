FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y python3-venv && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv

ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD [ "bash" ]