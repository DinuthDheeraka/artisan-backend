from fastapi import Request
from fastapi.responses import JSONResponse


# handle application exceptions
async def handle_application_exceptions(request: Request, exc: Exception):
    # handle ApplicationServiceException
    if isinstance(exc, ApplicationServiceException):
        print('here')
        return JSONResponse(status_code=exc.code,
                            content={"success": exc.success, "status_code": exc.code, "message": exc.message})

    # handle Exception
    if isinstance(exc, Exception):
        return JSONResponse(status_code=500, content={"success": False, "status_code": 500, "message": str(exc)})


# custom exception classes
class ApplicationServiceException(Exception):
    def __init__(self, code, success, message):
        super().__init__()
        self.code = code
        self.success = success
        self.message = message
