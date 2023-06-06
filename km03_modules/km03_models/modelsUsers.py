from .modelsBase import Base, sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# from itsdangerous.serializer import Serializer
from itsdangerous.url_safe import URLSafeTimedSerializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app



def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]



class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    image_file = Column(String(100),nullable=False, default='default.jpg')
    password = Column(String(100), nullable=False)
    timeStamp = Column(DateTime, default=datetime.now)
    permission = Column(Text)
    theme = Column(Text)
    # posts = relationship('Post', backref='author', lazy=True)
    track_inv = relationship('Tracking_inv', backref='updator_inv', lazy=True)
    track_re = relationship('Tracking_re', backref='updator_re', lazy=True)
    query_string_inv = relationship('Saved_queries_inv', backref='query_creator_inv', lazy=True)
    query_string_re = relationship('Saved_queries_re', backref='query_creator_re', lazy=True)

    # def get_reset_token(self, expires_sec=1800):
    def get_reset_token(self):
        # s=Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # s = jwt.encode(current_app.config['SECRET_KEY'], algorithm="HS256")

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        # payload = {"user_id": 5}
        # return serializer.dumps({'user_id': self.id}).decode('utf-8')
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        # s=Serializer(current_app.config['SECRET_KEY'])
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            # user_id = s.loads(token)['user_id']
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None
        # return Users.query.get(user_id)
        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f"Users('{self.id}','{self.email}','{self.permission}')"


class Investigations(Base):
    __tablename__ = 'investigations'
    id = Column(Integer, primary_key=True)
    NHTSA_ACTION_NUMBER=Column(String(10))
    MAKE=Column(String(25))
    MODEL=Column(String(256))
    YEAR=Column(Integer)
    COMPNAME=Column(Text)
    MFR_NAME=Column(Text)
    ODATE=Column(Date, nullable=True)
    CDATE=Column(Date, nullable=True)
    CAMPNO=Column(String(9))
    SUBJECT=Column(Text)
    SUMMARY=Column(Text)
    km_notes=Column(Text)
    date_updated = Column(DateTime, nullable=False, default=datetime.now)
    files = Column(Text)
    categories=Column(Text)
    linked_records=Column(Text)
    source_file=Column(Text)
    source_file_notes=Column(Text)
    km_tracking_id = relationship('Tracking_inv', backref='update_inv_record', lazy=True)
    

    def __repr__(self):
        return f"Investigations('{self.id}',NHTSA_ACTION_NUMBER:'{self.NHTSA_ACTION_NUMBER}'," \
        f"'SUBJECT: {self.SUBJECT}', ODATE: '{self.ODATE}', CDATE: '{self.CDATE}')"
    

class Tracking_inv(Base):
    __tablename__ = 'tracking_inv'
    id = Column(Integer, primary_key=True)
    field_updated = Column(Text)
    updated_from = Column(Text)
    updated_to = Column(Text)
    updated_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    time_stamp = Column(DateTime, nullable=False, default=datetime.now)
    investigations_table_id=Column(Integer, ForeignKey('investigations.id'), nullable=False)
    
    def __repr__(self):
        return f"Tracking_inv(investigations_table_id: '{self.investigations_table_id}'," \
        f"field_updated: '{self.field_updated}', updated_by: '{self.updated_by}')"

class Saved_queries_inv(Base):
    __tablename__ = 'saved_queries_inv'
    id = Column(Integer, primary_key=True)
    query_name = Column(Text)
    query = Column(Text)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    used_count =Column(Integer)
    
    def __repr__(self):
        return f"Km_saved_queries(id: '{self.id}', 'query_name: '{self.query_name}'," \
        f"query_creator_id: '{self.created_by}')"


class Recalls(Base):
    __tablename__ = 'recalls'
    RECORD_ID = Column(Integer, primary_key=True)
    CAMPNO=Column(Text)
    MAKETXT=Column(Text)
    MODELTXT=Column(Text)
    YEAR=Column(Integer)
    MFGCAMPNO=Column(Text)
    COMPNAME=Column(Text)
    MFGNAME=Column(Text)
    BGMAN =Column(Date, nullable=True)
    ENDMAN =Column(Date, nullable=True)
    RCLTYPECD=Column(Text)
    POTAFF=Column(Float)
    ODATE=Column(Date, nullable=True)
    INFLUENCED_BY=Column(Text)
    MFGTXT=Column(Text)
    RCDATE=Column(Date, nullable=True)
    DATEA=Column(Date,nullable=True)
    RPNO=Column(Text)
    FMVSS=Column(Text)
    DESC_DEFECT=Column(Text)
    # CONSEQUENCE_DEFCT=Column(Text) #<-- name changed Jun 2023
    CONSEQUENCE_DEFECT=Column(Text)
    CORRECTIVE_ACTION=Column(Text)
    NOTES=Column(Text)
    RCL_CMPT_ID=Column(Text)
    #not in production or dev
    MFR_COMP_NAME=Column(Text)
    MFR_COMP_DESC=Column(Text)
    MFR_COMP_PTNO=Column(Text)
    #end not in 
    km_notes=Column(Text)
    date_updated = Column(DateTime, nullable=False, default=datetime.now)
    files = Column(Text)
    categories=Column(Text)
    linked_records=Column(Text)
    source_file=Column(Text)
    source_file_notes=Column(Text)
    km_tracking_id = relationship('Tracking_re', backref='update_re_record', lazy=True)
    

    def __repr__(self):
        return f"Recalls('{self.RECORD_ID}',MAKE:'{self.MAKETXT}'," \
        f"'Component Name: {self.COMPNAME}', Manuf Name: '{self.MFGNAME}', Recall Date: '{self.RCDATE}')"

    

class Tracking_re(Base):
    __tablename__ = 'tracking_re'
    id = Column(Integer, primary_key=True)
    field_updated = Column(Text)
    updated_from = Column(Text)
    updated_to = Column(Text)
    updated_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    time_stamp = Column(DateTime, nullable=False, default=datetime.now)
    recalls_table_id=Column(Integer, ForeignKey('recalls.RECORD_ID'), nullable=False)

    
    def __repr__(self):
        return f"Tracking_re(id: '{self.id}'," \
        f"field_updated: '{self.field_updated}', updated_by: '{self.updated_by}')"

class Saved_queries_re(Base):
    __tablename__ = 'saved_queries_re'
    id = Column(Integer, primary_key=True)
    query_name = Column(Text)
    query = Column(Text)
    used_count =Column(Integer)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    
    def __repr__(self):
        return f"Km_saved_queries(id: '{self.id}', 'query_name: '{self.query_name}'," \
        f"query_creator_id: '{self.created_by}')"

