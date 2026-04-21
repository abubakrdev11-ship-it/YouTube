# YouTube-like Backend API

This is a Django REST Framework backend for a YouTube-like platform with user management, video uploads, likes, views, and subscriptions.

## Features

- User registration and authentication (JWT)
- Video upload with age restrictions
- Like/unlike videos
- View tracking
- Subscription system
- Swagger documentation

## Installation

1. Clone the repository
2. Install dependencies:
   `
   pip install -r requirements.txt
   `
3. Run migrations:
   `
   python manage.py migrate
   `
4. Create superuser:
   `
   python manage.py createsuperuser
   `
5. Run server:
   `
   python manage.py runserver
   `

## API Endpoints

- /api/schema/swagger-ui/ - Swagger UI documentation
- /api/token/ - Obtain JWT token
- /api/token/refresh/ - Refresh JWT token
- /api/users/users/ - User management
- /api/users/subscriptions/ - Subscription management
- /api/posts/videos/ - Video CRUD
- /api/posts/videos/{id}/like/ - Like/unlike video
- /api/posts/videos/{id}/view/ - View video

## Models

### User (CustomUserModel)
- username, email, avatar, date_of_birth, date_joined

### Video
- author, title, description, video_file, thumbnail, created_at, age_rating, views_count, likes_count

### Like
- user, video, created_at

### Views
- user, video, timestamp

### Subscription
- subscriber, subscribed_to, created_at

## Age Restrictions

Videos have age ratings:
- G: General Audience
- PG: Parental Guidance
- R: Restricted

## Authentication

Use JWT tokens for authentication. Obtain token from /api/token/ endpoint.
