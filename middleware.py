from fastapi import Request
from fastapi.responses import JSONResponse

from failure_manager import failure_manager


async def exception_middleware(request: Request, call_next):

    try:
        response = await call_next(request)
        return response

    except Exception as e:

        failure_manager.log_failure(e)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
                "error": str(e)
            }
        )