import sqlalchemy as sa
from sqlalchemy import orm
from .base import myBase

class CleaningSchedule(myBase):
    __tablename__ = 'cleaning_schedule'
    __table_args__ = (
        sa.PrimaryKeyConstraint('employee_id', 'floor_number', 'schedule_date', name='cleaning_schedule_pk'),
    )

    employee_id = sa.Column(sa.Integer,
                            sa.ForeignKey('employees.employee_id',
                                          name='employees_fk',
                                          ondelete='cascade',
                                          onupdate='cascade'),
                            nullable=False)
    floor_number = sa.Column(sa.Integer, nullable=False)
    schedule_date = sa.Column(sa.Date, nullable=False)

    employee = orm.relationship('Employee')

