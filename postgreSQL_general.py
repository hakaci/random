import psycopg2

from config import (DATABASE_1,
                    POSTGRESQL_USERNAME,
                    POSTGRESQL_PASSWORD,
                    POSTGRESQL_HOST,
                    POSTGRESQL_PORT
                    )


def import_sql_file(sql_file, dbname, user, password, host, port):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()

        # Read .sql file
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()

        # Execute SQL commands
        cursor.execute(sql_content)
        conn.commit()

        print(f"Successfully imported {sql_file} into PostgreSQL.")

    except psycopg2.Error as e:
        print(f"Error importing {sql_file} into PostgreSQL:", e)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def create_database(dbname, user, password, host, port):
    try:
        # Connect to PostgreSQL (use default 'postgres' database to create new database)
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
        conn.autocommit = True
        cursor = conn.cursor()

        # Create new database
        cursor.execute(f"CREATE DATABASE {dbname}")

        print(f"Successfully created database '{dbname}'.")

    except psycopg2.Error as e:
        print(f"Error creating database '{dbname}':", e)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Enter PostgreSQL connection details
    dbname = 'fart'
    user = POSTGRESQL_USERNAME
    password = POSTGRESQL_PASSWORD
    host = POSTGRESQL_HOST
    port = POSTGRESQL_PORT
    sql_file = DATABASE_1

    # create_database(dbname, user, password, host, port)
    import_sql_file(sql_file, dbname, user, password, host, port)
