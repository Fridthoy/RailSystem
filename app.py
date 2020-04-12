from flask import Flask, request, render_template
from pathFinder import *

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def example():
    if request.method == 'POST':
        global points
        global obsticles
        points = request.form['points']
        obsticles = request.form['obsticles']
        heights =  request.form['heights']
        print('mine points er  ' + points)
        print('mine obst er  ' + obsticles)
        results = heights.split(',')
        print(list(map(int, results)))
        return '<h1>Submitted</h1>'

    return render_template('index.html')

if __name__ == '__main__':
    app.run()



