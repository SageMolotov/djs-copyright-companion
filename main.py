import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from database import setup_database, get_track_status, update_track_status
from rekordbox import get_all_track_paths, add_tag_to_track
from api_client import check_community_database
import os

MUSIC_FOLDER = './music_to_watch'

class NewFileHandler(FileSystemEventHandler):
    """Event handler for new files in the music folder."""
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.mp3'):
            file_path = event.src_path
            print(f"Detected new file: {file_path}")
            process_new_track(file_path)

def process_new_track(file_path):
    """Handles the entire workflow for a new track."""
    # 1. Check local database first
    status = get_track_status(file_path)
    if status:
        print(f"Track already processed. Status: {status}")
        return

    # 2. Extract metadata (simplified)
    # In a real app, you would use a library like 'mutagen' to read ID3 tags.
    artist = "Unknown Artist"
    title = os.path.basename(file_path).split('.')[0]
    track_data = {'artist': artist, 'title': title, 'file_path': file_path}

    # 3. Query community database
    api_response = check_community_database(track_data)
    
    if api_response['status'] == 'found':
        copyright_status = api_response['claim']
        print(f"Community database has a match. Status: {copyright_status}")
        
        # 4. Update local database and Rekordbox
        update_track_status(file_path, copyright_status, "Community Database")
        tag = f"DJCC-{copyright_status}"
        add_tag_to_track(file_path, tag)
    else:
        print("No match in community database. Queuing for manual test.")
        update_track_status(file_path, "PENDING_TEST", "Local Queue")

def start_watcher():
    """Starts the file system watcher."""
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, MUSIC_FOLDER, recursive=True)
    observer.start()
    print(f"Watching for new files in: {MUSIC_FOLDER}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    # Initial setup
    setup_database()
    
    # Create the music folder if it doesn't exist
    if not os.path.exists(MUSIC_FOLDER):
        os.makedirs(MUSIC_FOLDER)
        print(f"Created music folder at: {MUSIC_FOLDER}")
        
    start_watcher()