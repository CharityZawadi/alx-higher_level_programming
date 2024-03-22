#!/usr/bin/python3
"""Fetches all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and print them with their corresponding state names
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).first().name
        print("{}: ({}) {}".format(
            state_name, city.id, city.name
        ))
