from project.settings import db

class Order(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.Text, nullable=False)
    surname = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    poshta = db.Column(db.Text, nullable=False)
    wishes = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}"