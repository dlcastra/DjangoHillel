import time


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)

        stop = time.time()
        execution_time = stop - start

        log = f"PATH:{request.path}, METHOD:{request.method}, EXECUTION TIME:{execution_time}\n"

        with open("logs.txt", "a") as log_data:
            log_data.write(log)

        return response
