#!/usr/bin/python3
''' python script
    that prints all City objects from the database hbtn_0e_14_usa
'''
from sys import argv

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for st, ct in session.query(State, City).\
            filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(st.name, ct.id, ct.name))

    session.close()
