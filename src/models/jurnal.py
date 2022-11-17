from extensions import db

class Jurnal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    transactions = db.relationship("Transaction", backref='transaction')

    def __repr__(self) -> str:
        return self.name