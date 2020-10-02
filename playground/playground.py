from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')        
def hello_world():
    return '<h1>Try typing the following lines after the 5000 in local host! /PLAY, OR /play/(your number), OR /play/(your number)/(your favorite color)</h1>' 


@app.route('/play')
def play():
    return render_template('index.html')


@app.route('/play/<int:num>')
def play2(num):
    return render_template('index.html', num = num)


@app.route('/play/<int:num>/<string:color>')
def play3(num,color):
    return render_template('index.html', num = num, color = color)
if __name__=="__main__":  
    app.run(debug=True)
