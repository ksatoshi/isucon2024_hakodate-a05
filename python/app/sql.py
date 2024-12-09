import os

import sqlalchemy

host = os.getenv("ISUCON_DB_HOST", "192.168.0.12")
port = int(os.getenv("ISUCON_DB_PORT", "3306"))
user = os.getenv("ISUCON_DB_USER", "isucon")
password = os.getenv("ISUCON_DB_PASSWORD", "isucon")
dbname = os.getenv("ISUCON_DB_NAME", "isuride")

slave_host = "192.168.0.13"
slave_port = 3306
slave_user = "isucon"
slave_password = "isucon"
slave_dbname = "isuride"

engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
)

slave_engine =sqlalchemy.create_engine(
        f"mysql+pymysql://{slave_user}:{slave_password}@{slave_host}:{slave_port}/{slave_dbname}"
)

