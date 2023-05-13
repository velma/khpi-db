
import click
from datetime import date
from datetime import timedelta
from queries import common
from scripts import database
from api.engine import DBConn
from models.base import myBase

# IMPORTANT: all models should be imported before the call to
#            myBase.metadata.create_all();
#            otherway no tables will be created
from models import *

@click.group()
def cli():
    #dotenv.load_dotenv()
    DBConn()


@cli.command(help='Создать таблицы в БД')
def create_tables():
    myBase.metadata.create_all(DBConn.engine)


@cli.command(help='Удалить таблицы в БД')
def drop_tables():
    myBase.metadata.drop_all(DBConn.engine)

@cli.command(help='Клієнти, які проживають у заданому номері')
@click.option('--room', '-r', type=click.STRING, prompt=True)
def list_clients_by_room(room):
    common.list_clients_in_room(room)

@cli.command(help='Клієнти, які прибули із заданого міста')
@click.option('--city', '-city', type=click.STRING, prompt=True)
def list_clients_by_city(city):
    common.list_client_from_city(city)

@cli.command(help='Хто із службовців прибирав номер вказаного клієнта у заданий день')
@click.option('--client_id', '-c', type=click.INT, prompt=True, default=1)
@click.option('--date', '-d', type=click.DateTime(formats=["%Y-%m-%d"]),
              prompt=True, default=str(date.today() + timedelta(days=1)))
def find_employee_cleaned_room(client_id, date):
    common.find_employee_cleaner_at_day(client_id, date)

@cli.command(help='Чи є в готелі вільні місця та вільні номери і, якщо є, то скільки')
def count_free_rooms():
    common.count_free_rooms()

@cli.command(help='Заполнить БД тестовыми данными')
def fill_db():
    database.fill_db()

if __name__ == '__main__':
    cli()
