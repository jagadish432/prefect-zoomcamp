from prefect_sqlalchemy import SqlAlchemyConnector, ConnectionComponents, SyncDriver



sql_connection= SqlAlchemyConnector(
   connection_info = ConnectionComponents(
        driver=SyncDriver.POSTGRESQL_PSYCOPG2,
        database="ny_taxi",
        username="root",
        password="root",
        host="127.0.0.1",
        port="5432",
    )
)

print(sql_connection.get_engine())

sql_connection.save("zoom-postgresql-connection", overwrite=True)
