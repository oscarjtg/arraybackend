from abc import ABC


class ArrayBackend(ABC):
    def array(self, array_like, dtype=None):
        raise NotImplementedError
