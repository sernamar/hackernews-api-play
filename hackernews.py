import requests
import json
import psycopg2
from psycopg2 import sql  # we need to import the whole SQL module this way


BASE_URL = "https://hacker-news.firebaseio.com/v0/item/"
TABLE_NAME = "items"


def get_item_from_api(id):
    url = BASE_URL + str(id) + ".json"
    response = requests.get(url)
    return json.loads(response.text)


def get_item_from_db(id):
    try:
        # Get the database credentials from the environment variable
        # DATABASE_URL = os.environ["DATABASE_URL"]
        DATABASE_URL = "postgresql://user:password@host/database"

        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_URL)

        # Open a cursor to perform database operations
        cursor = connection.cursor()

        # Write the query expression
        query = sql.SQL(
            "SELECT * FROM {table} WHERE item_id=%s").format(table=sql.Identifier(TABLE_NAME))

        # Query the database
        cursor.execute(query, [id])

        # Fetch one record
        item = cursor.fetchone()  # cursor.fetchall() to get all records

        # Make the changes to the database persistent
        # (not necessary in this example, as we'll just reading data)
        # connection.commit()

        # Return the item
        return item

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")
