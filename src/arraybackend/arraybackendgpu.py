import cupy as cp

from .interface import ArrayBackend


class ArrayBackendGPU(ArrayBackend):
    def array(self, array_like, *args, **kwargs):
        return cp.array(array_like, *args, **kwargs)
