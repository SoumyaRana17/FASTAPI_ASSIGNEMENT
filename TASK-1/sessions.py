
from sqlmodel import SQLModel,Session,create_engine

engine=create_engine(url="sqlite:///item.db",echo=True,connect_args={"check_same_thread":False})

def create_db_and_table():
   SQLModel.metadata.create_all(bind=engine)
   
   
   
def get_session():
   with Session(engine) as db:
      yield db 