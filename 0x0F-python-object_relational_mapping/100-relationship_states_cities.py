#!/usr/bin/python3
""" python script """

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    new_st = State(name='California')
    city = City(name='San Francisco')
    new_st.cities = [city]
    session.add(new_st)
    session.commit()
    session.close()
