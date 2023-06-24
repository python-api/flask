class MakeResponse:
    def __init__(self) -> None:
        pass
    def success(self):
        if type(self) is dict:
            return self
        else:
            return {'item': self}

    def failure(self):
        return {
            'errors': self
        }
