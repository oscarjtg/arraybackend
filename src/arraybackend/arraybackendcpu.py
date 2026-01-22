import numpy as np

from .interface import ArrayBackend


class ArrayBackendCPU(ArrayBackend):
    def array(self, array_like, dtype=None):
        return np.array(array_like, dtype=dtype)
