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
# curl http://<hostname.com>/locate_numbers?number=+13101231234

# For the output.csv
# You can use the django command like this
# docker ps
# Look for the cointainer id of exam
# docker exec -ti container-id bash
# python manage.py output_to_csv


# Solution
# With this exam I have noticed that the parameter number is not really found in phonenumbers it doesn't have the location compare to the possible result which is (213) 416-0509 this number can be found in phonenumbers and match with Los Angeles, having said that I created a model named Location and defined that this parameter number which is +13101231234 has a location of Los Angeles.

# I also created a models and those are Location and Number running in posgresql, the Location is the list of the location inside the csv number that has a valid location and I have created Many to Many relationship because some of the number has a more that one location listed in phonenumbers library.

# I also implemented the celery task and rabbitmq as broker because the phonenumbers is taking long during the POST method request to this endpoint http://<hostname.com>/locate_numbers it has now a better implementation compare for not having a celery task.
