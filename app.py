from flask import Flask, render_template, url_for, flash, redirect
from forms import FlairForm
from model import get_flair

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = []


@app.route("/",methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    global posts
    if len(posts)==10:
        posts=[]
    form = FlairForm()
    flag=False
    if form.validate_on_submit():
        d={}
        d['flair']=get_flair(form.URL.data)
        d['URL']=form.URL.data
        posts=[d]+posts
        return redirect(url_for('Flair_Detected'))
    return render_template('flair.html', form=form)


@app.route("/Flair_Detected")
def Flair_Detected():
    return render_template('flair_detected.html',posts=posts)

@app.route("/data1")
def data1():
    return render_template('data_analysis.html')

@app.route("/data2")
def data2():
    return render_template('da_2.html')

if __name__ == '__main__':
    app.run(debug=True)
