from flask import Flask
from flask import render_template
from flask import request

from block import write_block,check_integrity,show_data

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        Team1 = request.form.get('Team1')
        Team2 = request.form.get('Team2')
        Score = request.form.get('Score')
        Time = request.form.get('Time')
        print(Team1)
        print(Team2)
        print(Time)
        write_block(Team1=Team1, Team2=Team2, Score=Score, Time=Time)

    return render_template('index.html')

@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('index.html', checking_results=results)

@app.route('/show')
def show_db():
    data = show_data()
    return render_template('index.html', show=data)

if __name__ == '__main__':
    app.run(debug=True)
