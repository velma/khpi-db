import sqlalchemy as sa
from sqlalchemy import orm
from .base import myBase

class Visit(myBase):
    __tablename__ = 'visits'
    __table_args__ = (
        sa.PrimaryKeyConstraint('visit_id', name='visits_pk'),
    )

    id = sa.Column(sa.Integer, name='visit_id', autoincrement=True)
    room_id = sa.Column(sa.Integer,
                        sa.ForeignKey('rooms.room_id',
                                      name='rooms_fk',
                                      ondelete='cascade',
                                      onupdate='cascade'),
                        nullable=False)
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date, nullable=True)

    room = orm.relationship('Room')
    clients = orm.relationship('Client', secondary='visit_clients')

