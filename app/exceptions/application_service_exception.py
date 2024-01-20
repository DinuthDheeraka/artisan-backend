class ApplicationServiceException(Exception):
    def __init__(self, success, code, message):
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
