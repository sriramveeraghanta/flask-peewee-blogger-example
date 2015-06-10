from peewee import *

def get_db():
	database = SqliteDatabase('Blog.db')
	database.connect()
	return database

database=get_db()

class BaseModel(Model):
    class Meta:
        database = database

class BlogPost(BaseModel):
    title = CharField()
    text = TextField()

class Hello(BaseModel):
	name= TextField()
	phno= TextField()


if __name__ == '__main__':
	BlogPost.create_table()
	Hello.create_table()
