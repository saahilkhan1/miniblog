# Mini Blog Platform

A simple blogging API built using**Django** with features like user authentication, CRUD operations on posts, likes, comments, and complete Dockerization for easy local dev.

---

## Features

- User Registration & Login (Token-based)
- Authenticated users users can create, edit, delete their own blog posts
- Public view of blog posts after login
- Like and commment on other users’ posts
- REST API for posts (GET, POST, PUT, DELETE)
- Strict validation and error handling
- Postman collection
- Dockerizer for setup and deployment

---

## 🛠️ Project Structure
mini_blog_project/
├── posts/ # Blog posts app
│ ├── migrations/ # DB migrations for posts, likes, comments
│ ├── serializers.py # Serializers for posts, likes, comments
│ ├── models.py # Blog, Like, Comment models
│ ├── views.py # API views for CRUD posts, likes, comments
│ └── urls.py # Posts-related API routes
├── mini_blog_project/ # Project config (settings, urls, wsgi)
│ ├── settings.py # Django settings (DB, installed apps, middleware)
│ ├── urls.py # Project-level URL routing (include user/posts)
│ └── wsgi.py # WSGI entrypoint
├── manage.py # Django CLI runner
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image config (if dockerized)
├── docker-compose.yml # Docker compose file for web + db
├── README.md # Project documentation & instructions
└── docs/ # Postman collection, API specs


# **Clone the repo**
```bash
git clone https://github.com/saahilkhan1/miniblog
1 install requirement.txt
2. Create virtual environment
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver


# API Endpoints
```bash
Endpoint	Method  Description	Auth Required

/api/register/	POST	Register new user	No
/api/login/	POST	User login, get auth token	No
/api/posts/	GET	List all blog posts	Yes
/api/posts/	POST	Create new blog post	Yes
/api/posts/<id>/	GET	Get specific post (own posts only)	Yes
/api/posts/<id>/	PUT	Edit own blog post	Yes
/api/posts/<id>/	DELETE	Delete own blog post	Yes
/api/posts/<id>/like/	POST	Like/unlike a post	Yes
/api/posts/<id>/comment/	POST	Add comment to a post	Yes


# API postaaman collection
Import the Postman collection in   https://blue-firefly-988972.postman.co/workspace/My-Workspace~64bfad59-3cd9-4f86-8311-284a4467d47e/collection/27157812-792d9a21-cb46-44ab-98e0-007336b55eee?action=share&creator=27157812    to test all APIs easily.


# Environment Variables change credentials according to your database
DB_NAME=miniblog
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your-secret-key







