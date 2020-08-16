from wsgiref.simple_server import make_server
from webob import Request, Response


class App:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        current_path = request.path
        response = Response()

        for path, handler in self.routes.items():
            if path == current_path:
                handler(request, response)
                return response

        self.default_response(response)
        return response

    def default_response(self, response):
        response.status = 404
        response.text = '404. Not found...'

    def serve(self, host='localhost', port=8000):
        try:
            server = make_server(host, port, app=self.__call__)
            server.serve_forever()
        except KeyboardInterrupt:
            print('Goodbye! :)')
        except:
            print('Something bad was happened')
        finally:
            exit()
