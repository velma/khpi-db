
import datetime

from api.engine import DBConn
from models.employee import Employee
from models.client import Client
from models.room import Room
from models.visit import Visit
from models.cleaning_schedule import CleaningSchedule

def fill_db():
    with DBConn.get_session() as session:
        employee1 = Employee(last_name='Bloggs', first_name='Joe')
        employee2 = Employee(last_name='Schmoe', first_name='Joe')

        session.add(employee1)
        session.add(employee2)
        session.flush()

        client1 = Client(last_name='Doe', first_name='John', passport='SM11111', city='New York')
        client2 = Client(last_name='Doe', first_name='Jane', passport='SM22222', city='New York')
        client3 = Client(last_name='Unknown', first_name='Name', passport='SM3333', city='Paris')

        session.add(client1)
        session.add(client2)
        session.add(client3)
        session.flush()

        room1 = Room(room_number='101', floor_number=1, phone='+38011111111')
        room2 = Room(room_number='102a', floor_number=1, phone='+38011111112')
        room3 = Room(room_number='102b', floor_number=1, phone='+38011111113')
        room4 = Room(room_number='201', floor_number=2, phone='+38011111114')
        room5 = Room(room_number='301', floor_number=3, phone='+38011111115')
        room6 = Room(room_number='302', floor_number=3, phone='+38011111116')

        session.add(room1)
        session.add(room2)
        session.add(room3)
        session.add(room4)
        session.add(room5)
        session.add(room6)
        session.flush()

        visit1 = Visit(room_id=room1.id,
                       start_date=datetime.date.today() - datetime.timedelta(days=10),
                       end_date=datetime.date.today() - datetime.timedelta(days=7),
                       clients=[client3])
        visit2 = Visit(room_id=room1.id,
                       start_date=datetime.date.today() - datetime.timedelta(days=5),
                       end_date=datetime.date.today() - datetime.timedelta(days=2),
                       clients=[client3])
        visit3 = Visit(room_id=room1.id, start_date=datetime.date.today(), clients=[client3])
        visit4 = Visit(room_id=room2.id, start_date=datetime.date.today(), clients=[client1, client2])

        session.add(visit1)
        session.add(visit2)
        session.add(visit3)
        session.add(visit4)
        session.flush()

        schedule1 = CleaningSchedule(employee_id=employee1.id,
                                     floor_number=1,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=1))
        schedule2 = CleaningSchedule(employee_id=employee1.id,
                                     floor_number=2,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=1))
        schedule3 = CleaningSchedule(employee_id=employee2.id,
                                     floor_number=3,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=1))
        schedule4 = CleaningSchedule(employee_id=employee1.id,
                                     floor_number=1,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=2))
        schedule5 = CleaningSchedule(employee_id=employee2.id,
                                     floor_number=2,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=2))
        schedule6 = CleaningSchedule(employee_id=employee2.id,
                                     floor_number=3,
                                     schedule_date=datetime.date.today() + datetime.timedelta(days=2))

        session.add(schedule1)
        session.add(schedule2)
        session.add(schedule3)
        session.add(schedule4)
        session.add(schedule5)
        session.add(schedule6)
        session.commit()