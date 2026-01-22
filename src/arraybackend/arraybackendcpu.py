import numpy as np

from .interface import ArrayBackend


class ArrayBackendCPU(ArrayBackend):
    def array(self, array_like, *args, **kwargs):
        return np.array(array_like, *args, **kwargs)
