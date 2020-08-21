!/bin/bash

# entrypoint bash script for docker-compose 

echo "Waiting for theater database ..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "theater database started ..."


else if [ "$ENVIRONMENT" == "production" ]
then
  echo "launching production server"
  gunicorn theater_api.wsgi:app\
           --bind 0.0.0.0:443

else if [ "$ENVIRONMENT" == "development" ]
then
  echo "launching development server"
  gunicorn theater_api.wsgi:app\
           --bind 0.0.0.0:443\
           --reload
else
  echo "(entrypoint.sh) ENVIRONMENT has value: $ENVIRONMENT
This environment is not implemented."
fi