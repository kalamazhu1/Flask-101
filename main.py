from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  name = ''
  if request.method == 'POST':
    name = request.form['name']
  return render_template('index.html', name=name)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
