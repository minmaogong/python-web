import subprocess
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from table_2_models import Departments, Employees
#创建数据库引擎
db_host = "localhost"
db_port = 3306

db_name = "fastapi_db"
db_user_name = "root"
db_password = "123456"
url =f"mysql+pymysql://{db_user_name}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
engine = create_engine(url, echo=True)


#配置会话工厂
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine, autocommit=False,autoflush=False)

