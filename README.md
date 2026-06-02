# Task 17 - Error Handling Middleware

## Objective
Handle backend failures gracefully using middleware, retry handlers, and failure tracking.

## Features

- Global Exception Middleware
- Retry Mechanism
- Failure Logging
- Structured JSON Responses
- FastAPI Backend

## Technologies

- Python
- FastAPI
- Uvicorn

## Endpoints

### GET /
Returns application status.

### GET /test-error
Simulates a backend failure.

### GET /failures
Displays logged failures.

## Run

pip install -r requirements.txt

uvicorn main:app --reload