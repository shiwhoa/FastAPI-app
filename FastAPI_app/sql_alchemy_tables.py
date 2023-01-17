from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base


sql_alchemy_table_engine = declarative_base()

class SQL_Alchemy_Postgres_Posts_Table(sql_alchemy_table_engine): # Post extends Base
    __tablename__ = 'posts'

    sql_alchemy_id = Column(Integer, primary_key=True, nullable=False)
    sql_alchemy_title = Column(String, nullable=False)
    sql_alchemy_content = Column(String, nullable=False)
    sql_alchemy_published = Column(Boolean, server_default='True', nullable=False)
    sql_alchemy_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    sql_alchemy_user_id = Column(Integer, ForeignKey("users.sql_alchemy_user_id", ondelete = "CASCADE"), nullable= False)

    sql_alchemy_user = relationship("SQL_Alchemy_Postgres_User_Table") # does not create anything in the table but allows in pydantic to relate these 2 tables

class SQL_Alchemy_Postgres_User_Table(sql_alchemy_table_engine):
    __tablename__ = 'users'
    sql_alchemy_user_id = Column(Integer, primary_key=True, nullable=False)
    sql_alchemy_user_email = Column(String, nullable=False, unique=True)
    sql_alchemy_user_password = Column(String, nullable=False)
    sql_alchemy_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


# class SQL_Alchemy_Postgres_Votes_Table(sql_alchemy_table_engine):
#     __tablename__ = 'votes'
#     sql_alchemy_liked_by_user_id = Column(Integer, ForeignKey("users.sql_alchemy_user_id", ondelete = "CASCADE"), nullable = False, primary_key=True)
#     sql_alchemy_liked_post_id = Column(Integer, ForeignKey("posts.sql_alchemy_id", ondelete = "CASCADE"), nullable = False, primary_key=True)


# class SQL_Alchemy_Postgres_Votes_Table(sql_alchemy_table_engine):
#     __tablename__ = 'votes'
#     sql_alchemy_liked_by_user_id = Column(Integer, ForeignKey("users.alembic_user_id", ondelete = "CASCADE"), nullable = False, primary_key=True)
#     sql_alchemy_liked_post_id = Column(Integer, ForeignKey("posts.alembic_id", ondelete = "CASCADE"), nullable = False, primary_key=True)