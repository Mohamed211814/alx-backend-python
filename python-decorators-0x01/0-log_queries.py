
import sqlite3
import functools

Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract and log the query argument if it exists
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            print(f"[LOG] Executing SQL Query: {query}")
        else:
            print("[LOG] No SQL query found.")
        return func(*args, **kwargs)
    return wrapper

Function that fetches users with query logging
log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

Fetch users (and log the query)
users = fetch_all_users(query="SELECT * FROM users")
