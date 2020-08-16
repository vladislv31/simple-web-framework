from app import App


app = App()


@app.route('/')
def index(req, resp):
    resp.text = 'Index page'

@app.route('/about')
def index(req, resp):
    resp.text = 'About page'

@app.route('/google')
def index(req, resp):
    resp.status = 307
    resp.location = 'http://google.com'


app.serve()
