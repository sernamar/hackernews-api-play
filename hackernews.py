import requests
import os
from psycopg2 import connect, sql, Error as psycopg2_error


BASE_URL = "https://hacker-news.firebaseio.com/v0/item/"
TABLE_NAME = "items"


def get_comment_from_api(id):
    url = BASE_URL + str(id) + ".json"
    response = requests.get(url)
    return response.text


def get_comment_from_db(id):
    try:
        # Get the database credentials from the DATABASE_URL environment variable
        DATABASE_URL = os.environ["DATABASE_URL"]

        # Connect to an existing database
        connection = connect(DATABASE_URL)

        # Open a cursor to perform database operations
        cursor = connection.cursor()

        # Write the query
        query = sql.SQL(
            "SELECT * FROM {table} WHERE item_id=%s").format(table=sql.Identifier(TABLE_NAME))
        # Query the database
        cursor.execute(query, [id])

        # Fetch one record
        comment = cursor.fetchone()  # cursor.fetchall() to get all records

        # Make the changes to the database persistent
        # (not necessary in this example, as we'll just reading data)
        # connection.commit()

        # Return the comment
        return comment

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")
