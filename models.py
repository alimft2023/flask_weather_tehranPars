from peewee import SqliteDatabase, Model, IntegerField, FloatField, CharField, DateField


db = SqliteDatabase('weather.db')


class Weather(Model):
    temp = FloatField()
    pressure = IntegerField()
    humidity = IntegerField()
    description = CharField(max_length=20)
    date = DateField()
    icon = CharField(max_length=10)
    city = CharField(max_length=10)

    class Meta:
        database = db
        db_table = 'weather'


Weather.create_table()
