
from pathlib import Path
from shutil import move
from threading import Thread
import logging



folders = []
extensions = []


def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = base_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                move(el, new_path / el.name)
            except OSError as e:
                logging.error(e)

def del_empty_folders(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            try:
                el.rmdir()
            except OSError:
                pass





if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(input('Type path to folder:'))


    folders.append(base_folder)
    grabs_folder(base_folder)
    threads = []
    for folder in folders:
        th = Thread(target=sort_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    del_empty_folders(base_folder)
    print('The process has been finished successfully')