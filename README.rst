===========
Courier App
===========

Courier is a Django App to that conduct corier services. The application features both the 
admin as well as the user side. 

The application uses XAMMP MySQL (Database Server). 

Quick Start 
-----------
1. In order to use the application install the required prerequisites and dependencies via pip
much like presented below::
	
	``pip install django``
	``pip install mysqlclient``
	``pip install django_filter``
	``pip install xlwt``
	``pip install XlsxWriter``
	``pip install xlrd`` 
	``pip install xhtml2pdf`` 

django must be below version 4 

2. Include the "users" URLconf in your project urls.py like this::
	
	path('', include('users.urls')),

The database named "courier_app" must be created before proceeding to the next step. 

2. Run ``python manage.py makemigrations users`` in order to create the tables from within the 
models.py file.

3. Run the ``python manage.py migrate`` to complete the models.

4. In order to create a super user who has access to all of the application permissions, run 
``python manage.py createsuperuser`` the prompt will then ask for an email as well as password. 

5. Start the development server and visit http://127.0.0.1:8000/admin/ to access the admin panel 
which has access to all the web app features. Input the email and password. 

6. visit http://127.0.0.1:8000/ to proceed to the initial webpage of the application.