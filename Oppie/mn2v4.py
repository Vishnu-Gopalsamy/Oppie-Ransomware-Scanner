import csv
import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, csvfile):
        self.csvfile = csvfile

    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            print(f'A new file has been added: {event.src_path}')
            with open(self.csvfile, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([event.src_path])

    def on_moved(self, event):
        if event.is_directory:
            return None
        else:
            print(f'A file has been renamed: {event.dest_path}')
            with open(self.csvfile, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([event.dest_path])
if __name__ == '__main__':
    paths_to_monitor = [os.path.expanduser('~\\Downloads'), os.path.expanduser('~\\Documents')]
    disks_to_monitor = ['D:\\', 'E:\\']  # Replace with the desired disks

    csvfile = 'templates/buffer_filepath.csv'
    event_handler = NewFileHandler(csvfile)
    observer = Observer()

    for path in paths_to_monitor + disks_to_monitor:
        observer.schedule(event_handler, path, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()