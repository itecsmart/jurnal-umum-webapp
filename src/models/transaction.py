from extensions import db
from sqlalchemy.types import Date


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(Date)
    description = db.Column(db.String(100))
    debt = db.Column(db.Integer, default=0)
    kredit = db.Column(db.Integer, default=0)
    jurnal_id = db.Column(db.Integer, db.ForeignKey('jurnal.id'))

    def __repr__(self):
        return self.description