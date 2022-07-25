import psycopg2
import psycopg2.extras

from functions import find_last_id_client
from functions import find_last_id_purchase


class DataBaseManager:

    @staticmethod
    def add_client(name: str,
                   last_name: str,
                   birthday: str,
                   money_spent: str):

        try:
            connection = psycopg2.connect(
                host='localhost',
                database='data_base',
                user='postgres',
                password=''
            )

            new_id = int(find_last_id_client()) + 1

            cur = connection.cursor()
            postgres_insert_query = (' INSERT INTO customers (name, last_name, birthday, money_spent, id)'
                                     ' VALUES (%s,%s,%s,%s,%s)')

            record_to_insert = (name, last_name, birthday, money_spent, new_id)
            cur.execute(postgres_insert_query, record_to_insert)

            connection.commit()

            cur.close()
            connection.close()

        except ConnectionError:
            pass

    @staticmethod
    def delete_client(client_id: str):

        try:
            connection = psycopg2.connect(
                host='localhost',
                database='data_base',
                user='postgres',
                password=''
            )

            cur = connection.cursor()

            cur.execute(' DELETE FROM customers WHERE id = %s', client_id)

            connection.commit()

            cur.close()
            connection.close()

        except ConnectionError:
            pass

    @staticmethod
    def add_purchase(client_id: str, goods_id: str, quantity: str, price: str):

        try:
            connection = psycopg2.connect(
                host='localhost',
                database='data_base',
                user='postgres',
                password=''
            )

            new_id = int(find_last_id_purchase()) + 1

            cur = connection.cursor()
            postgres_insert_query = (' INSERT INTO purchases (client_id, goods_id, quantity, price, id)'
                                     ' VALUES (%s,%s,%s,%s,%s)')

            record_to_insert = (client_id, goods_id, quantity, price, new_id)
            cur.execute(postgres_insert_query, record_to_insert)

            connection.commit()

            cur.close()
            connection.close()

        except ConnectionError:
            pass

    @staticmethod
    def print_all_purchases_by_id(client_id: str):

        try:
            connection = psycopg2.connect(
                host='localhost',
                database='data_base',
                user='postgres',
                password=''
            )

            cur = connection.cursor()
            postgres_find_query = ' select goods_id, quantity, price from purchases where client_id = %s'

            cur.execute(postgres_find_query, client_id)

            connection.commit()

            results = cur.fetchall()

            for row in results:
                print(row)

            cur.close()
            connection.close()

        except ConnectionError:
            pass


if __name__ == '__main__':
    # DataBaseManager.add_client('bartosz', 'nowak', '2003-03-13', '300')
    # DataBaseManager.delete_client('2')
    # DataBaseManager.add_purchase('1', '1', '10', '10')
    # DataBaseManager.print_all_purchases_by_id('1')





