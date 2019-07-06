# pip install sqlalchemy Установка библиотеки

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timedelta

Base = declarative_base()
engine = create_engine('postgresql://postgres:123456789@localhost/test_bd')
Session = sessionmaker(bind=engine)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    start_at = Column(Date, nullable=False)
    tags = Column(JSONB, server_default='[]', default=list, nullable=False)

    def __str__(self):
        return f'{self.id}: {self.name}: {self.start_at}: {self.tags}'

    def __repr__(self):
        return f'{self.id}: {self.name}: {self.start_at}: {self.tags}'


session = Session()
# res = session.query(Course).all()
# print(res)
#
# for course in res:
#     print(course)


def create_all():
    Base.metadata.create_all(engine)

def drop_all():
    Base.metadata.drop_all(engine)

# drop_all()
create_all()

def add_course(**kwargs):
    course = Course(**kwargs)
    print(f'ДО: {course}')
    session.add(course)
    session.commit()
    print(f'После: {course}')

def add_coursrs():
    now_date = datetime.now().date()
    add_course(name='python',
               start_at=now_date,
               tags=['program'])
    add_course(name='SMM',
               start_at=now_date + timedelta(days=5),
               tags=['marketig'])

# add_coursrs()

def find_courses(tag_to_find='program'):
    query = session.query(Course)

    print(f'Good courses {tag_to_find}')
    filter_query = query.filter(Course.tags.has_key(tag_to_find))
    for course in filter_query.all():
        print(course)

# find_courses('marketig')

def find_courses_name(name=''):
    query = session.query(Course).filter(Course.name == name)
    for course in query.all():
        print(course)

find_courses_name('python')