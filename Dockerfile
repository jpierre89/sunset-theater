FROM python:3

ENV PYTHONUNBUFFERED 1 PYTHONDONTWRITEBYTECODE 1

# for entrypoint
RUN apt-get update && apt-get install -y netcat

ENV HOME=/home

WORKDIR $HOME
COPY . .
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

CMD ["bash", "./entrypoint.sh"]