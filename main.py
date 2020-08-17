from app import App


app = App()


@app.route('/')
def index(req, resp):
    resp.text = app.get_template('index.html', name='name', title='Title of the page')

@app.route('/about')
def index(req, resp):
    resp.text = app.get_template('about.html')

@app.route('/google')
def index(req, resp):
    resp.status = 307
    resp.location = 'http://google.com'


app.serve()
