from config.db_config import get_connection
from model.model_module import Customer
from exceptions.exceptions import EntityNotFoundException


class ClientRepository:

    def save_client(self, customer):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO customers(first_name,last_name) VALUES(%s, %s)"
            val = (customer.firstName, customer.lastName)
            cursor.execute(sql, val)
            connection.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            connection.close()

    def get_all_client(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            sql = "SELECT * FROM customers"
            cursor.execute(sql)

            client_list = []
            for client_tuple in cursor.fetchall():
                client_list.append(Customer(client_tuple[0], client_tuple[1], client_tuple[2]))

            return client_list
        finally:
            cursor.close()
            connection.close()

    def get_client_by_id(self, client_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM customers WHERE id = %s ", (client_id,))

            client_tuple = cursor.fetchone()
            if client_tuple is None:
                raise EntityNotFoundException("Entity Not Found!")
            return Customer(client_tuple[0], client_tuple[1], client_tuple[2])
        finally:
            cursor.close()
            connection.close()

    def update_client(self, client_id, first_name, last_name):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(" UPDATE customers SET first_name = %s, last_name = %s  WHERE id = %s ",
                           (first_name, last_name, client_id))
            return cursor.rowcount
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    def delete_client(self, client_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM customers WHERE id = %s ", (client_id,))

            return cursor.rowcount
        finally:
            connection.commit()
            cursor.close()
            connection.close()
