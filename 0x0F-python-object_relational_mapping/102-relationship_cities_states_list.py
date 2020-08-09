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

    for state in session.query(City.id, City.name, State.name) \
            .join(State.cities) \
            .order_by(City.id) \
            .all():
        print("{}: {} -> {}".format(state[0], state[1], state[2]))

    session.close()
