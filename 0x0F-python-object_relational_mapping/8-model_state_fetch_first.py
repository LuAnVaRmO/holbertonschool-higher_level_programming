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
    instance = session.query(State).first()

    if instance is None:
        print("Nothing")
    else:
        print("{}: {}".format(instance.id, instance.name))

    session.close()
