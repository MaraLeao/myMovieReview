# My Movie Review

## Description

**My Movie Review** is a Django project that allows users to search for movie information and add their own reviews. Users can search for movies by title, view details about the returned movie, and submit a review with their name, rating, and comments. Reviews are stored in a database and can be edited, deleted, or viewed later.

## Features

- **Movie Search**: Allows users to search for movies by title and obtain detailed information about the movie.
- **Review Submission**: Users can add a review for the movie, including their name, rating (from 1 to 5), and a comment.
- **Review Management**: Reviews can be edited, deleted, or viewed in a list.

## Technologies Used

 - **Django**: Web framework used for project development.
 - **OMDB API**: API used to obtain movie information.
 - **SQLite**: Database used to store reviews.

## Project Setup

### Requirements

- Python 3.x
- Django 3.x or higher

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/my-movie-review.git
   cd my-movie-review
   
2. **Create a Virtual Environment and Install Dependencies**
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate     # For Windows
   pip install -r requirements.txt
   
3. **Configure Environment Variables**
- Add your OMDB API key to the configuration file (settings.py).

### Using the OMDB API
- To obtain movie information, the project uses the OMDB API. The process to use the API is as follows:
1. Obtain an API Key
  - Visit the OMDB API website and request an API key. You will need to provide only an email address to receive the key.
 2. Make the Request
   - The following code snippet makes a request to the API and retrieves information about a movie:
     ```bash
     import requests
     
     def getMovie(self, title):
        response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&t={title}')
    
        if response.status_code == 200:
            data_movie = response.json()
            return {
                'poster': data_movie.get('Poster'),
                'title': data_movie.get('Title'),
                'type': data_movie.get('Type'),
                'release': data_movie.get('Released'),
                'plot': data_movie.get('Plot'),
                'language': data_movie.get('Language'),
                'genre': data_movie.get('Genre'),
                'director': data_movie.get('Director'),
                'writer': data_movie.get('Writer'),
                'actors': data_movie.get('Actors'),
                'awards': data_movie.get('Awards')
            }
        return None
     
### Running the Project

1. Apply Migrations
   ```bash
   python manage.py migrate
   
2. Start the server
   ```bash
   python manage.py runserver
   
3. Acess the aplication
  - Open a browser and go to http://127.0.0.1:8000/ to start using My Movie Review.

## Project Structure

The project is organized into several key files and directories. Below is an overview of the main components:

### `myMovieReview/`

This is the root directory of the Django project, containing project-specific settings and configurations.

- **`__init__.py`**: Marks the directory as a Python package.
- **`asgi.py`**: ASGI configuration for handling asynchronous tasks.
- **`settings.py`**: Contains project settings, including database configurations, static files settings, and installed apps.
- **`urls.py`**: Defines URL patterns for the project, routing requests to the appropriate views.
- **`wsgi.py`**: WSGI configuration for serving the application in a WSGI-compatible web server.

### `movies/`

The Django application directory (replace `movies` with the name of your application if different).

- **`__init__.py`**: Marks the directory as a Python package.
- **`admin.py`**: Register models for the Django admin interface.
- **`apps.py`**: Contains application-specific configurations.
- **`forms.py`**: Defines forms used in the application, including movie search and review forms.
- **`models.py`**: Defines the database models. Includes the `Movie` model for storing movie reviews.
- **`tests.py`**: Contains test cases for the application.
- **`urls.py`**: Defines URL patterns for the application.
- **`views.py`**: Contains the business logic for handling requests and rendering responses. Includes the `MoviePages` class for fetching movie data and managing reviews.

### `templates/`

Contains HTML templates used to render views.

- **`index.html`**: Template for the main page where users can search for movies and submit reviews.
- **`review_detail.html`**: Template for displaying detailed information about a specific review.
- **`review_list.html`**: Template for displaying a list of all reviews.
- **`review_confirm_delete.html`**: Template for confirming the deletion of a review.
- **`edit_review.html`**: Template for editing an existing review.

### `manage.py`

A command-line utility that lets you interact with this Django project. You can use it to run the server, apply migrations, create superusers, and more.

### `README.MD`
- This file, providing an overview of the project, setup instructions, and other important information.

### `requirements.txt`

- A file listing the Python packages required for the project. Install these dependencies using:
  ```bash
  pip install -r requirements.txt

### `LICENSE`
- Contains the license information for the project.

This section describes the directory structure and key files in your Django project, providing a clear overview of how the project is organized. Adjust the file and directory names as needed to match your actual project structure.