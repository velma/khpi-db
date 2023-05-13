import sqlalchemy as sa
from .base import myBase


class Employee(myBase):
    __tablename__ = 'employees'
    __table_args__ = (
        sa.PrimaryKeyConstraint('employee_id', name='employees_pk'),
        sa.CheckConstraint('status IN (\'active\', \'inactive\')', name='employee_status_ck')
    )

    id = sa.Column(sa.Integer, name='employee_id', autoincrement=True)
    last_name = sa.Column(sa.String(50), nullable=False)
    first_name = sa.Column(sa.String(50), nullable=False)
    status = sa.Column(sa.String(8), nullable=False, server_default='active')

    def __repr__(self):
        return f'<Employee(id={self.id}, last_name={self.last_name}, first_name={self.first_name}, status={self.status})'