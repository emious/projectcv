Command you needed

uvicorn projectcv.asgi:application --reload

celery -A  projectcv beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery -A projectcv worker -l info 

# ProjectCV

Welcome to **ProjectCV**! This project is designed to demonstrate an application that uses Celery for asynchronous task processing, Celery Beat for periodic tasks, WebSocket for real-time communication, and Docker for containerization.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Install Dependencies](#1-install-dependencies)
  - [2. Docker Setup](#2-docker-setup)
- [Usage](#usage)
  - [1. Running the Application](#1-running-the-application)
  - [2. Celery and Celery Beat](#2-celery-and-celery-beat)
- [Contributing](#contributing)
- [License](#license)

## Features

- Asynchronous task processing with Celery
- Periodic tasks scheduling with Celery Beat
- Real-time communication using WebSocket
- Containerization with Docker

## Requirements

- Docker
- Docker Compose

## Setup

### 1. Install Dependencies

Make sure you have Docker and Docker Compose installed on your system. You can download and install Docker from [Docker's official site](https://www.docker.com/get-started), and Docker Compose from [Docker Compose's official documentation](https://docs.docker.com/compose/install/).

### 2. Docker Setup

Clone the repository:

```bash
git clone https://github.com/emious/projectcv.git
cd projectcv
```

make .env
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_PASSWORD=
DJANGO_SUPERUSER_EMAIL=
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 [::1]
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432
EMAIL_PASS=
EMAIL=



Build and run the Docker containers:
```bash
docker-compose up --build
```

This will start all necessary services, including:

The web server
Celery worker
Celery Beat
WebSocket server
Usage

1. Running the Application
Once the Docker containers are up and running, you can access the application at http://localhost:8000.

2. Celery and Celery Beat
Celery and Celery Beat will automatically start as defined in the docker-compose.yml file.

To manually start Celery workers or Celery Beat, you can use the following commands

```bash
celery -A  projectcv beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A projectcv worker -l info 
```

for websockets work you must run
```bash
uvicorn projectcv.asgi:application --reload
```

#Contributing

We welcome contributions to ProjectCV! If you have suggestions, bug fixes, or improvements, please submit a pull request or open an issue.

#License

This project is licensed under the MIT License - see the LICENSE file for details.

