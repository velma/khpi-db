import sqlalchemy as sa
import datetime

from api.engine import DBConn
from models.employee import Employee
from models.client import Client
from models.room import Room
from models.visit import Visit
from models.cleaning_schedule import CleaningSchedule
from sqlalchemy import select

#клієнти, які проживають у заданому номері,
def list_clients_in_room(room_number):
    with DBConn.get_session() as session:
        clients = session.execute(
            select(Client)
            .join(Visit.clients)
            .join(Room)
            .where(Visit.end_date == None)
            .where(Visit.start_date >= datetime.date.today())
            .where(Room.room_number == room_number)
        )
        for client in clients:
            print(client)

#клієнти, які прибули із заданого міста
def list_client_from_city(city):
    with DBConn.get_session() as session:
        clients = session.execute(
            select(Client)
            .where(Client.city == city)
        )
        for client in clients:
            print(client)

#хто із службовців прибирав номер вказаного клієнта у заданий день
def find_employee_cleaner_at_day(client_id, date):
    with DBConn.get_session() as session:
        floor_stmt = select(Room.floor_number).join(Visit.room).join(Visit.clients).where(Client.id == client_id)

        employees = session.execute(
            select(Employee)
            .join(CleaningSchedule.employee)
            .where(CleaningSchedule.schedule_date == date)
            .where(CleaningSchedule.floor_number.in_(floor_stmt))
        )
        for employee in employees:
            print(employee)

#чи є в готелі вільні місця та вільні номери і, якщо є, то скільки.
def count_free_rooms():
    with DBConn.get_session() as session:
        count = session.execute(
            select(sa.func.count(Room.id))
            .where(~sa.exists(select(Visit).where(Room.id == Visit.room_id).where(Visit.end_date == None)))
        ).scalar()

        print(count)