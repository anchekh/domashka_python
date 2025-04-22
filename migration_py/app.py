from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Student

@app.route('/')
def index():
    students = Student.query.order_by(Student.last_name).all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)