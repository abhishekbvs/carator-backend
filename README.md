# Carator-Backend
Carator is an organization for Accounting professionals. This is a application which manages all the work they do and collobarate people to make things easier. In this repository, backend of the application is built using django. One need to install python, django and other dependencies to run this project. It's recommended to create a virtual environment and start running.

### Installation Instructions
1. Install Python3 and pip
2. Install `virtualenvwrapper` and add it to your terminal path.
3. Clone the repository and create the virtual environment
    ```
      $ git clone https://github.com/abhishekbvs/carator-backend.git
      $ cd carator-backend
      $ mkvirtualenv --python=python3 carator
      $ workon carator
    ```
4. Install the dependencies from `requirements.txt`
    ```
      $ pip install -r requirements.txt
    ```
### Running the Application
1. Start the virtual environment `workon carator`
2. Set up the database
    ```
      python manage.py migrate
    ````
3. Create super user
    ```
      python manage.py createsuperuser
    ```
4. Run the project
    ```
      python manage.py runserver
    ```
### API's
Using GraphQL, API is designed
