from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_wsRaH9f-pWSVw4kvRRy@mysql-19ac5bf0-utxicotepec-b6a5.l.aivencloud.com:18583/defaultdb"

#  Conexión local
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
