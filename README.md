# Library Management API

## Overview

The Library Management API is a RESTful web application for managing a collection of books in a library. The application provides features to add, list, search, update, and delete books. It includes Swagger-based API documentation for easy interaction with the endpoints.

This application is dockerized for simplified deployment and portability.

## Features

- Add a new book to the library.

- List all books with their details.

- Search for books by author, published year, or genre.

- Delete a book using its ISBN.

- Update book details using its ISBN.

- Interactive API documentation using Swagger UI.

## Prerequisites

1. Docker installed on your system.

2. Postman or any HTTP client (optional, for testing).

## Getting Started

1. Clone the Repository
```
git clone <repository_url>
cd library-management-api
```

2. Build the Docker Image
```
docker build -t library-api .
```

3. Run the Docker Container
```
docker run -d -p 5000:5000 --name library-api-container library-api
```

The application will now be running and accessible at `http://localhost:5000`.

## API Endpoints

**Base URL: http://localhost:5000**

### 1. Add a New Book

**POST `/books`**

- Request Body (JSON):
```
{
  "title": "Book Title",
  "author": "Author Name",
  "published_year": 2023,
  "isbn": "123456789",
  "genre": "Fiction"
}
```

- Response (JSON):
```
{
  "message": "Book added successfully",
  "book": {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2023,
    "isbn": "123456789",
    "genre": "Fiction"
  }
}
```

### 2. List All Books

**GET `/books`**

- Response (JSON):
```
[
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2023,
    "isbn": "123456789",
    "genre": "Fiction"
  }
]
```

### 3. Search for Books

**GET `/books?author=Author+Name&genre=Fiction`**

- Query Parameters:

  - author (optional): Filter by author.
  
  - published_year (optional): Filter by published year.
  
  - genre (optional): Filter by genre.

- Response (JSON):
```
[
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2023,
    "isbn": "123456789",
    "genre": "Fiction"
  }
]
```

### 4. Update Book Details

**PUT `/books/<isbn>`**

- Request Body (JSON):
```
{
  "title": "Updated Title"
}
```

- Response (JSON):
```
{
  "message": "Book updated successfully",
  "book": {
    "title": "Updated Title",
    "author": "Author Name",
    "published_year": 2023,
    "isbn": "123456789",
    "genre": "Fiction"
  }
}
```

### 5. Delete a Book

**DELETE `/books/<isbn>`**

- Response (JSON):
```
{
  "message": "Book deleted successfully"
}
```

## Swagger Documentation

The API documentation is available via Swagger UI:

- URL: `http://localhost:5000/api-docs`

Swagger provides an interactive interface to explore and test the API endpoints.

## Development Notes

### Running Locally without Docker

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
python app.py
```

3. Access the application at `http://localhost:5000`.

## Stopping and Removing the Docker Container

**Stop the container:**
```
docker stop library-api-container
```

**Remove the container:**
```
docker rm library-api-container
```

## Contributing

1. Fork the repository.

2. Create a new branch for your feature/bugfix.

3. Submit a pull request with detailed information about your changes.

