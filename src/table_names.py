from sqlalchemy import create_engine
from src.constants import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING)
print(engine.table_names())