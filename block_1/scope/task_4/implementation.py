def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывает и закрывает файл

    Args:
        file_path: путь до файла
    """
    open = bad_open
    ###
    # Добавьте свой код сюда
    ###
    f = open(file_path, 'r')
    f.close()
