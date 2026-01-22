from abc import ABC


class ArrayBackend(ABC):
    def array(self, array_like, *args, **kwargs):
        raise NotImplementedError
