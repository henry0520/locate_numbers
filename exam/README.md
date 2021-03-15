# Instruction how to deploy
# unzip the exam zip file
# ~ cd exam
# ~ docker-compose build
# ~ docker-compose run -p 80:80 -d exam

# check the swagger for the api endpoint
# http://<hostname.com>/api/swagger

# To test the endpoint, the postman is recommended

# http://<hostname.com>/admin/
# test credential
# username: henry
# email: henry@gmail.com
# passwd: 1234

# Once you have uploaded the file to http://<hostname.com>/locate_numbers
# Wait for more or less 10 minutes to finished the job task in the background
# After 10 minutes the data is available and you can curl it like below:
# curl http://<hostname>/locate_numbers?number=+13101231234

# For the output.csv
# You can use the django command like this
# docker ps
# Look for the cointainer id of exam
# docker exec -ti container-id bash
# python manage.py output_to_csv
