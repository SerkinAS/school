import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade_level = Column(Integer)
    classes = relationship("Class", secondary='enrollment', back_populates="students")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    school_id = Column(Integer, ForeignKey('schools.id'))
    login = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    classes = relationship("Class", secondary='enrollment', back_populates="students")
    user_id = Column('User', ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __repr__(self):
        return f"Student {self.full_name()}"


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    subject_taught = Column(String)
    classes = relationship("Class", back_populates="teacher")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Teacher {self.letter} {self.number}"


class SchoolClass(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    letter = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="classes")
    students = relationship("Student", secondary='enrollment', back_populates="classes")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Class {self.letter} {self.number}"


class Rate(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    class_id = Column(Integer, ForeignKey('classes.id'))
    to_class = relationship("Class", back_populates="assignments")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Rate {self.id}"
