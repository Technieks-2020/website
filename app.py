from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/events')
def events():
  return render_template('events.html')

@app.route('/scoreboard')
def scoreboard():
  return render_template('scoreboard.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/live')
def live():
  return render_template('live.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 