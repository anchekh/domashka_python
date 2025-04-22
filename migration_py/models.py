from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Студент {self.last_name} {self.first_name} {self.surname}>'