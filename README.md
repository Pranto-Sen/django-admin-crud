## Introduction
This project is a Django-based CRUD (Create, Read, Update, Delete) application designed to manage hotel data. It allows you to store and manage property information, including images, amenities, and locations. This application integrates with a Scrapy project that scrapes hotel data from external sources, stores it in a PostgreSQL database, and downloads images to local storage. The Django application provides an admin interface to manage the scraped data, including migrating the data from the Scrapy database to the Django database and handling image storage.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/Pranto-Sen/django-admin-crud.git
    cd django-admin-crud
    ```

2. **Create a virtual environment:**

    - On Windows, create and activate the virtual environment:
      ```bash
       py -3 -m venv .venv
      .venv\Scripts\activate
      ```

    - On Linux/Mac, create and activate the virtual environment:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```


3. **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Navigate to the Project Directory**
    ```
    cd myproject
    ```
   **Folder Structure**

    ```
     myproject/
        │
        ├── media/
        │   └── hotel_images/
        │
        ├── myapp/
        │   ├── management/
        │   │   └── commands/
        │   │       ├── download_images.py
        │   │       └── migrate_hotels.py
        │   │
        │   ├── migrations/
        │   │
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        │
        ├── myproject/
        │ 
        ├── .env
        ├── .env.sample
        └── manage.py

    ```

6. **Create the .env file in the root directory of the project, where manage.py and .env.sample are located** 
    - First, create the database and specify the ```DJANGO_DATABASE_NAME``` value in the .env file. Execute the SQL command to create the database: ```CREATE DATABASE 
        database_name;```
    - In the previous assignment, you already ran the project, which automatically created a database and stored the scraped information. Now, use this database for the 
       ```SCRAPY_DATABASE_NAME```
    - The Scrapy project images are stored in a folder named ```hotel_images``` located on the local storage. You can navigate inside this ```hotel_images``` folder to access 
          the images. After navigating inside this ```hotel_images``` folder, copy the path and paste it as ```SOURCE_FOLDER```
    - If the image path is: `/home/w3e37/Desktop/tripdotcom-hotel-scraper/trip_scraper/hotel_images/image_1.jpg` 
         Then set  `/home/w3e37/Desktop/tripdotcom-hotel-scraper/trip_scraper/hotel_images`

      ```sql
      
        # Django database connection details
        DJANGO_DATABASE_NAME = Django database name
        DATABASE_USER = PostgreSQL database username
        DATABASE_PASSWORD = password
        DATABASE_HOST = Hostname 
        DATABASE_PORT = Portnumber 
        
        # Name of the database used by the Scrapy project
        SCRAPY_DATABASE_NAME= Scrapy database name
        
        # Path to the directory where Scrapy project images are stored
        SOURCE_FOLDER=        
      
      ```
  
      
7. **Create Migrations for Your App**
    ```
    python manage.py makemigrations 
    ```
8. **Apply Migrations**
    ```
    python manage.py migrate
    ```
9. **Run the Superuser Creation Command**
    ```
    python manage.py createsuperuser
    ```

10. **Migrate data from scrapy database**
    ```
    python manage.py migrate_hotels
    ```

11. **Save scrapy image folder from local storage to django project**
    ```
    python manage.py download_images
    ```
    
12. **Run the Development Server** 
    ```
    python manage.py runserver
    ```
13. **Go to this URL** 
    ```
    http://127.0.0.1:8000/admin
    ```          
