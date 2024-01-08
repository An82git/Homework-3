from threading import Thread
from pathlib import Path
import logging


DIR_PATH = Path("D:/Хлам")

threads = []

def new_thread_folder(dir_path: Path) -> None:
    thread = Thread(target=sort_folder, args=(dir_path,))
    threads.append(thread)
    thread.start()


def new_thread_move(path: Path) -> None:
    thread = Thread(target=move_file, args=(path,))
    threads.append(thread)
    thread.start()


def move_file(path: Path) -> None:
    move_path = DIR_PATH.joinpath(path.suffix.upper().removeprefix("."))
    if not move_path.exists():
        move_path.mkdir()
    path.rename(move_path.joinpath(path.name))
    logging.debug("Ending a file move thread.")


def sort_folder(dir_path: Path) -> None:
    for path in dir_path.iterdir():
        if path.is_file():
            new_thread_move(path)
        else:
            new_thread_folder(path)
    logging.debug("Ending the folder iteration flow.")


def remove_folder(path: Path) -> None:
    for namber in range(2):
        for file in path.glob("**/*"):
            try:
                file.rmdir()
            except OSError:
                remove_folder(file)


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.debug("Start of the program.")

    new_thread_folder(DIR_PATH)

    [el.join() for el in threads]

    logging.debug("Completion of all threads.")

    remove_folder(DIR_PATH)

    logging.debug("End of the program.")


if __name__ == "__main__":
    main()
