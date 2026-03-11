class APIClient:
    def __init__(self, request_context):
        self.request = request_context

    def create_user(self, payload: dict):
        return self.request.post("/users", data=payload)