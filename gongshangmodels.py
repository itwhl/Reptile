from sqlalchemy import Column, Integer, String

from database import Base


class GongShangXinXi(Base):
    __tablename__ = 'tb_gongshang_xinxi'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    gs_name = Column(String(255))
    falv_ren = Column(String(255))
    chengli_riqi = Column(String(255))
    jy_status = Column(String(255))
    gs_type = Column(String(255))
    gs_hangye = Column(String(255))
    dj_jiguan = Column(String(255))
    zc_dizhi = Column(String(255))
    xinyong_daima = Column(String(255))
    gs_zhucehao = Column(String(255))
    zc_ziben = Column(String(255))
    sj_ziben = Column(String(255))

