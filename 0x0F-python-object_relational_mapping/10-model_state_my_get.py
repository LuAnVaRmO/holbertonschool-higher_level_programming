#!/usr/bin/python3
""" python script """

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    st_name = argv[4]
    state = session.query(State).filter_by(name=st_name).first()
    print(state.id) if state else print('Not found')
    session.close()
