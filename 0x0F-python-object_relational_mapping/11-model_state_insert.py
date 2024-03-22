#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Add Louisiana state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)
