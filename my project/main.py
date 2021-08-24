from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
  return render_template('home.html')

@app.route('/about/')

def about():
    return render_template('about.html')

@app.route('/class10/')

def class10():
    return render_template('class10.html')

@app.route('/class10quiz/')

def class10quiz():
    return render_template('class10quiz.html')

if __name__ == '__main__':
   app.run(debug=True)