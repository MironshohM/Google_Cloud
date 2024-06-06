# from config import DB_HOST, DB_NAME, DB_USER, DB_PASS
# import mysql.connector
# from datetime import datetime

# db_connection = mysql.connector.connect(
#     host=DB_HOST,
#     user=DB_USER,
#     password=DB_PASS,
#     database=DB_NAME
# )
# db_cursor = db_connection.cursor()

# print("Successfull connection")


# # def save_message(user_id, username, message_text, message_url=None):
# #     timestamp = datetime.now()
# #     query = "INSERT INTO user_messages (user_id, username, message_text, message_time, message_url) VALUES (%s, %s, %s, %s, %s)"
# #     values = (user_id, username, message_text, timestamp, message_url)
# #     db_cursor.execute(query, values)
# #     db_connection.commit()


# def get_last_100_messages():
#     print("In function:")
#     query = "SELECT user_id, username, message_text, message_time, message_url " \
#             "FROM user_messages ORDER BY message_time DESC LIMIT 1000"
#     db_cursor.execute(query)
#     results = db_cursor.fetchall()

#     html_table = "<table border='1'>"
#     html_table += "<tr><th>User ID</th><th>Username</th><th>Message Text</th><th>Message Time</th><th>Message URL</th></tr>"
#     for row in results:
#         user_id, username, message_text, message_time, message_url = row
#         html_table += f"<tr><td>{user_id}</td><td>{username}</td><td>{message_text}</td><td>{message_time}</td><td>{message_url}</td></tr>"
#     html_table += "</table>"

#     return html_table
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import mysql.connector
from datetime import datetime

def connect_to_database():
  """Establishes a connection to the MySQL database."""
  try:
    db_connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    return db_connection
  except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    return None

def close_connection(db_connection):
  """Closes the connection to the MySQL database."""
  if db_connection:
    db_connection.cursor().close()
    db_connection.close()

def get_last_100_messages():
  """Fetches the last 100 messages and returns them as an HTML table."""
  print("In function:")
  db_connection = connect_to_database()
  if not db_connection:
    return None

  try:
    db_cursor = db_connection.cursor()
    query = "SELECT user_id, username, message_text, message_time, message_url " \
            "FROM user_messages ORDER BY message_time DESC LIMIT 1000"
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    html_table = "<table border='1'>"
    html_table += "<tr><th>User ID</th><th>Username</th><th>Message Text</th><th>Message Time</th><th>Message URL</th></tr>"
    for row in results:
        user_id, username, message_text, message_time, message_url = row
        html_table += f"<tr><td>{user_id}</td><td>{username}</td><td>{message_text}</td><td>{message_time}</td><td>{message_url}</td></tr>"
    html_table += "</table>"

    return html_table
  finally:
    close_connection(db_connection)

# # Example usage
# last_messages = get_last_100_messages()
# if last_messages:
#   print(last_messages)
# else:
#   print("Failed to retrieve messages.")
