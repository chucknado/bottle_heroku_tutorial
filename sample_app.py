import os

from bottle import Bottle, template, redirect, static_file

app = Bottle()


@app.route('/home')
def show_home():
    return template('home')


@app.route('/')
def handle_root_url():
    redirect('/home')


@app.route('/profile')
def make_request():
    # make an API request here
    profile_data = {'name': 'Marcel Hellkamp', 'role': 'Developer'}
    return template('details', data=profile_data)


@app.route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')


@app.error(404)
def error404(error):
    return template('error', error_msg='404 error. Nothing to see here')


if __name__ == '__main__':
    if 'DYNO' in os.environ:
       app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
    else:
       app.run(host='localhost', port=8080, debug=True)
