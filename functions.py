import psycopg2


def find_last_id_client():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='data_base',
            user='postgres',
            password=''
        )

        cur = connection.cursor()
        postgres_max_id_query = ' select max(id) from customers'

        cur.execute(postgres_max_id_query)

        l_id = (cur.fetchone()[0])

        connection.commit()

        cur.close()
        connection.close()

        return l_id

    except ConnectionError:
        pass


def find_last_id_purchase():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='data_base',
            user='postgres',
            password=''
        )

        cur = connection.cursor()
        postgres_max_id_query = ' select max(id) from purchases'

        cur.execute(postgres_max_id_query)

        l_id = (cur.fetchone()[0])

        connection.commit()

        cur.close()
        connection.close()

        return l_id

    except ConnectionError:
        pass
