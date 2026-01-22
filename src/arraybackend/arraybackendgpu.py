import cupy as cp

from .interface import ArrayBackend


class ArrayBackendGPU(ArrayBackend):
    def array(self, array_like, dtype=None):
        return cp.array(array_like, dtype=dtype)
