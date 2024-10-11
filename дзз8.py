from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URL"] = "mysql+pymysql://staschqi_1312:3%Mk1004@staschqi.beget.tech/staschqi_1312"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)




@app.route('/')
def index():
    return render_template('glavna.html')

@app.route('/post1')
def post1():
    return render_template('glavna2.html')

@app.route('/post2')
def post2():
    return render_template('glavna3.html')

@app.route('/post3', methods=["GET", "POST"])
def post3():
    return render_template('glavna4.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)