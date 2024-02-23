import nox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

@nox.session
def monitor_files(session):
    def on_file_change(event):
        if event.src_path.endswith('.md'):
            # Run your script or desired action here
            session.run('python', 'clean-markdown.py')

    observer = Observer()
    event_handler = FileSystemEventHandler()
    event_handler.on_modified = on_file_change
    observer.schedule(event_handler, path=os.path.join("content", "english", "lessons"))
    observer.start()
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
