import sqlalchemy as sa
from .base import myBase


class Client(myBase):
    __tablename__ = 'clients'
    __table_args__ = (
        sa.PrimaryKeyConstraint('client_id', name='clients_pk'),
        sa.UniqueConstraint('passport', name='passport_uk')
    )

    id = sa.Column(sa.Integer, name='client_id', autoincrement=True)
    last_name = sa.Column(sa.String(50), nullable=False)
    first_name = sa.Column(sa.String(50), nullable=False)
    passport = sa.Column(sa.String(15), nullable=False)
    city = sa.Column(sa.String(30), nullable=False)

    def __repr__(self):
        return f'<Client(id={self.id}, last_name={self.last_name}, first_name={self.first_name}, passport={self.passport}, city={self.city})'