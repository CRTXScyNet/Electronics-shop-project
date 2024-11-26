class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        print(f'Файл {args} поврежден')