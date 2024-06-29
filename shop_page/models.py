from project.settings import db

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key = True)

    name = db.Column(db.Text, nullable = False)
    discount = db.Column(db.Integer(), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    count = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"id: {self.id}"