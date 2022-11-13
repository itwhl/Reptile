from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'mysql://root:Whl.126@120.55.193.180:3306/GongShangXinXi?charset=utf8'

# 通过create_engine配置数据库引擎（如何驱动数据库）
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# 通过sessionmaker函数创建数据库会话工厂对象（创建访问数据库的Session对象）
db_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 通过declarative_base函数获取到一个模型类的元类
Base = declarative_base()