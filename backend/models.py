from sqlalchemy import Column, Integer, String
from backend.database import Base


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    file_path = Column(String)
class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    file_path = Column(String)