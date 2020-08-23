!/bin/bash

# entrypoint bash script for docker-compose 

echo "Waiting for theater database ..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "theater database started ..."


if [ "$ENVIRONMENT" == "production" ]
then
  echo "launching PRODUCTION server"
  gunicorn app:app --bind 0.0.0.0:8000
elif [ "$ENVIRONMENT" == "development" ]
then
  echo "launching DEVELOPMENT server"
  gunicorn app:app --bind 0.0.0.0:8000 --reload
else
  echo "(entrypoint.sh) ENVIRONMENT has value: $ENVIRONMENT
This environment is not implemented."
fi