from wsgiref.simple_server import make_server
from webob import Request, Response
import os
from jinja2 import Template
import core.vars as variables


class App:
    def __init__(self, templates_dir='templates', static_dir='static'):
        self.routes = {}
        self.templates_dir = templates_dir
        self.static_dir = static_dir

    def get_template(self, template_name, **kwargs):
        template_path = self.templates_dir + '/' + template_name

        with open(template_path, 'r') as f:
            content = f.read()

        template = Template(content)
    
        return template.render(**kwargs)

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

        if os.path.isdir(self.static_dir):
            static_files = []

            for r, d, f in os.walk(self.static_dir):
                for f_ in f:
                    static_files.append('/' + '/'.join([r, f_]))

            if current_path in static_files:
                static_file_ext = current_path.split('.')[-1]

                files_exts = variables.content_types

                with open(current_path.strip('/'), 'r') as f:
                    static_file_content = f.read()

                response.text = static_file_content
                response.content_type = 'text/html' if static_file_ext not in files_exts.keys() else files_exts[static_file_ext]

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
