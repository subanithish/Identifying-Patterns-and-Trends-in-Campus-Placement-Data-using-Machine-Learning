from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')


@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[int(request.form['sen1']), int(request.form['sen2']), int(request.form['sen3']),
               int(request.form['sen4']), float(request.form['sen5']), int(request.form['sen6'])]]
    # Perform machine learning prediction here using the input data
    # Return the predicted output value (0 or 1) to the second-page.html template
    return render_template('second-page.html', y=1)


if __name__ == '__main__':
    app.run(debug=True)
