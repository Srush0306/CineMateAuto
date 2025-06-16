# ✅ database.py
import mysql.connector

# Database connection setup
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",  # Use your own password if set
        database="cinemate"
    )

# Fetch movies and their show details
def fetch_movies_and_shows():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.title, m.genre, s.show_time, s.screen
        FROM shows s
        JOIN movies m ON s.movie_id = m.movie_id
    """)
    results = cursor.fetchall()
    conn.close()
    return results

# Book a ticket for a given movie show
def book_ticket(movie_id, customer_name, show_time, screen):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bookings (customer_name, movie_id, show_time, screen)
            VALUES (%s, %s, %s, %s)
        """, (customer_name, movie_id, show_time, screen))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Booking error:", e)
        return False

# Fetch all booking records with movie title
def fetch_all_bookings():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.booking_id, b.customer_name, m.title, b.show_time, b.screen
        FROM bookings b
        JOIN movies m ON b.movie_id = m.movie_id
    """)
    results = cursor.fetchall()
    conn.close()
    return results
