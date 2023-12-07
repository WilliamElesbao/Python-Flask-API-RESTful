from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30))
  age = db.Column(db.String(30))
  address = db.Column(db.String(120))

  def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'address': self.address
    }

