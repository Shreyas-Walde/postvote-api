# PostVote API

A backend clone of a social media application built with FastAPI and PostgreSQL.  
Features user authentication, post management, and a voting system similar to Reddit/Twitter.

## Overview

PostVote API is a RESTful backend service that allows users to register, log in, create posts, and upvote or remove votes from posts.  
It is designed as a learning project and demonstrates core social media backend features.


## Features

- 🔐 **User Authentication** - JWT-based authentication with secure password hashing
- 📝 **CRUD Operations** - Create, Read, Update, Delete posts
- 👍 **Voting System** - Upvote/unlike posts
- 🗄️ **PostgreSQL Database** - Robust data persistence with SQLAlchemy ORM
- 🔄 **Database Migrations** - Alembic for version-controlled schema changes
- 📖 **API Documentation** - Auto-generated Swagger UI and ReDoc

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy 1.4
- **Migrations:** Alembic
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Passlib + Bcrypt
- **Validation:** Pydantic

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL
- uv (recommended) or pip

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/postvote-api.git
   cd postvote-api
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   uv venv
   .venv\Scripts\activate  # Windows
   uv sync
   ```

3. **Create `.env` file in project root:**
   ```env
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_PASSWORD=your_password
   DATABASE_NAME=fastapi
   DATABASE_USERNAME=postgres
   SECRET_KEY=your_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

5. **Start the server:**
   ```bash
   fastapi dev app/main.py --reload
   ```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | User login |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users` | Create user |
| GET | `/users/{id}` | Get user by ID |

### Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/posts` | Get all posts |
| POST | `/posts` | Create post |
| GET | `/posts/{id}` | Get post by ID |
| PUT | `/posts/{id}` | Update post |
| DELETE | `/posts/{id}` | Delete post |

### Votes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/vote` | Vote on a post |

## API Documentation

Once the server is running, access:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Project Structure

```
learn-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── config.py        # Environment settings
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── oauth2.py        # JWT authentication
│   ├── utils.py         # Utility functions
│   └── routers/
│       ├── auth.py      # Authentication routes
│       ├── post.py      # Post routes
│       ├── user.py      # User routes
│       └── vote.py      # Vote routes
├── alembic/
│   └── versions/        # Database migrations
├── .env                 # Environment variables (not in repo)
├── .gitignore
├── pyproject.toml
└── README.md
```

## License

MIT License

## Author

Built while learning FastAPI 🚀