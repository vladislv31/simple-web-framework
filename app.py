from wsgiref.simple_server import make_server
from webob import Request, Response


class App:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = Response()
        response.text = 'Hello'

        return response(environ, start_response)

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
