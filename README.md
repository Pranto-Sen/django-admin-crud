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
        ├── .venv/
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
        ├── .env
        ├── .env.sample
        ├── .gitignore
        ├── manage.py
        └── requirements.txt

    ```

6. **Create the .env file in the root directory of the project, where manage.py and .env.sample are located** 

      ```sql
      # Django database connection details
        DJANGO_DATABASE_NAME=  # Name of the Django database
        DATABASE_USER=         # PostgreSQL database username
        DATABASE_PASSWORD=     # PostgreSQL database password
        DATABASE_HOST=         # Hostname for the database connection
        DATABASE_PORT=         # Port number for the PostgreSQL database
        
        # Scrapy project database name
        SCRAPY_DATABASE_NAME=  # Name of the database used by the Scrapy project
        
        # Source folder for Scrapy images
        SOURCE_FOLDER=         # Path to the directory where Scrapy project images are stored
      
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
