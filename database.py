import sqlite3

DATABASE_PATH = 'music_library.db'

def setup_database():
    """Initializes the SQLite database and creates the 'tracks' table."""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY,
            file_path TEXT NOT NULL UNIQUE,
            artist TEXT,
            title TEXT,
            copyright_status TEXT,
            source TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_track_status(file_path):
    """Checks the local database for a track's copyright status."""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT copyright_status FROM tracks WHERE file_path = ?", (file_path,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def update_track_status(file_path, status, source):
    """Inserts or updates a track's copyright status in the local database."""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO tracks (file_path, copyright_status, source) VALUES (?, ?, ?)", 
              (file_path, status, source))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    print("Database setup complete.")