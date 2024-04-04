from sqlalchemy import Table
from config import metadata,engine,Session


def insert_into_table(table_name, **kwargs):
   
    table = Table(table_name, metadata, autoload=True)

    with Session() as session:
        # Create an insert statement
        insert_statement = table.insert().values(**kwargs)
        session.execute(insert_statement)
        session.commit()
    

