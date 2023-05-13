import sqlalchemy as sa
from .base import myBase


class Room(myBase):
    __tablename__ = 'rooms'
    __table_args__ = (
        sa.PrimaryKeyConstraint('room_id', name='rooms_pk'),
        sa.UniqueConstraint('room_number', name='room_number_uk')
    )

    id = sa.Column(sa.Integer, name='room_id', autoincrement=True)
    room_number = sa.Column(sa.String(4), nullable=False)
    floor_number = sa.Column(sa.Integer, nullable=False)
    phone = sa.Column(sa.String)

