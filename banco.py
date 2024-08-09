from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./terremotos.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Terremoto(Base):
    __tablename__ = "terremotos"

    id = Column(Integer, primary_key=True, index=True)
    magnitude = Column(Float, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    localizacao = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
