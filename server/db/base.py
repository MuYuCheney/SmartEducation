from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from configs import SQLALCHEMY_DATABASE_URI
import json


# 构建和配置数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,

    # 将数据库操作结果（可能包含非 ASCII 字符）直接转换为 JSON 格式输出
    json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False),
)

# 工厂函数，用于创建与数据库的会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基类 Base，定义数据模型，这些模型将直接映射到数据库中的表
Base: DeclarativeMeta = declarative_base()
