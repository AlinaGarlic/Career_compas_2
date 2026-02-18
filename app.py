from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
  name='World'
  return render_template('index.html', name=name)

@app.route('/records')
def records():
    return 'Our records'

if __name__ == '__main__':
   app.run(debug=True)