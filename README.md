
# Movie Rating Webapp

This is a basic movie rating system built using Django.





## Features
##### Key Features: ( === solved and incompleteness ===)
- **( complete )** Log In: Create an account for authentication. 
- **( complete )** Add Movies: Add movies to the system, including title and  release year.
- **( complete )** View Movie List: See a list of all movies in the system.
- **( complete )** Rate Movies: Submit a rating (1-10 stars) for a specific movie.
- **( incomplete )** Search and View Details: Search for a specific movie by title and view its details.**( raise error - due to time shortage couldn't solved )**





#### Technologies:

- Backend: Django (Python web framework), Bootstrap4
- Database: SQLite



## Installation

- Create a virtual environment:
 ``` bash 
 python -m venv venv
 ```
- Activate the virtual environment: 
```
source venv/scripts/activate 
```
- Install dependencies: 
```
pip install -r requirements.txt
```
- Migrate database tables: 
```
python manage.py makemigrations
python manage.py migrate
```
- Create a superuser account (for initial admin access):
``` 
python manage.py createsuperuser
```
- Run server:
```
 python manage.py runserver
 ```

 
    
