from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/getdata', methods=['POST'])
def getdata():
    name1 = request.form['fname']
    name2 = request.form['lname']
    age = int(request.form['age'])
    print(name1, name2, int(age))
    if int(age) >= 18:
        text = str(name1)+str(name2)+" You are eligible to vote."
    else:
        text = str(name1)+str(name2)+" You are not eligible to vote."
    return render_template('output.html', output=text)

if __name__ == '__main__':
    app.run(debug=True)
