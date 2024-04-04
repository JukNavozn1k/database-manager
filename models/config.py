from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to your database
engine = create_engine('postgresql://gleb:root@vpn.glebtests.ru/postgres',echo=False)

# Create a MetaData object
metadata = MetaData()
metadata.reflect(bind=engine)
Session = sessionmaker(bind=engine)