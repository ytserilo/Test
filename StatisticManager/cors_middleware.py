class CORSMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/api/' and request.path == '':
            response["Access-Control-Allow-Origin"] = "*"
        else:
            response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000/"
        return response
