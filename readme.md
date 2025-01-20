## Technologies

- **Django**: Web framework for building the backend.
- **PostgreSQL**: Relational database to store the financial organizations' data.
- **Redis**: In-memory data store for caching and messaging.
- **Nginx**: Web server to serve the application.
- **Docker**: Containerization of the application for easy setup and deployment.
- **OpenPyXL**: Python library to read and parse Excel files.

## Prerequisites

Before getting started, you need to have the following installed:

- Docker
- Docker Compose
- Python 3.10 (for local development, if not using Docker)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/financial-orgs.git
cd financial-orgs
```

### 2. Set up environment variables

No need to create `.env` file. Already created.


### 3. Build and start the Docker containers

Run the following command to build and start all services:

```bash
docker-compose up --build
```

This will build the application image, set up PostgreSQL, Redis, Nginx, and start the Django web application.

### 4. Apply migrations

Once the containers are up, apply the migrations to set up the database:

```bash
docker-compose exec web python manage.py migrate
```

### 5. Import Financial Organizations

To import the financial organizations from the Excel file, run the following command:

```bash
docker-compose exec web python manage.py import_financial_orgs
```

Make sure that the `finOrgs.xlsx` file is in the correct location or specify the path if necessary.

### 6. Access the application

Once everything is set up, you can access the application in your browser:

```bash
http://localhost
```

The web interface should be available, and you can interact with the imported data.

## Usage

- **Django Admin**: Access the Django admin panel to manage the imported data at `http://localhost/admin`.
- **Database**: Use PostgreSQL to query and manipulate the data stored by the application.

## Development

To contribute or develop locally, you can follow these steps:

1. Install dependencies in your virtual environment:

```bash
pip install -r requirements.txt
```

2. Set up your local PostgreSQL database.
3. Run Django development server:

```bash
python manage.py runserver
```