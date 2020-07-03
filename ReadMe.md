This software is created by:
Austin Strain (1487409)
Jaffar, Kadir (0291141)
Aakarshan Simkhada (1898617)
Zainab Dadani (1304129)
..

It is built in Python with a Django framework.
 
Description: 

A partner of your company has requested to build a software application that will predict the fuel rate based on the following criteria:

- Client Location
- Competitors rate
- Client history
- Gallons requested
- Company profit margin (%)
- Seasonal rate fluctuation (%)

Software must include following components:

- Login (Allow Cleint to register if not a client yet)
- Cleint Registration (Initially only username and Password)
- Client Profile Management (After client registers they should login first to complete profile)
- Fuel Quote Form with Pricing module (Once user enters all required information pricing module predicts the rate)
- User Fuel Quote History

Initialize models before running server with commands:
python manage.py makemigrations
python manage.py migrate

Run server with this command:
python manage.py runserver

Runs on local host url or "127.0.0.1:800"

Library requirents:
pip install pillow
pip install django

