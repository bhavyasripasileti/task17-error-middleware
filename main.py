from fastapi import FastAPI

from middleware import exception_middleware
from retry_handler import retry
from failure_manager import failure_manager


app = FastAPI()

app.middleware("http")(exception_middleware)


@app.get("/")
def home():
    return {
        "message": "Task 17 Running"
    }


@retry(max_attempts=3)
def unstable_service():
    raise Exception("Database Connection Failed")


@app.get("/test-error")
def test_error():

    return unstable_service()


@app.get("/failures")
def failures():

    return {
        "count": len(failure_manager.get_failures()),
        "logs": failure_manager.get_failures()
    }