#!/usr/bin/python3
""" python script """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    row = session.query(State).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
    session.close()
