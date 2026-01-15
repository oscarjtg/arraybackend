# Array Backend

A Python package for calling different Python array backends using one single interface.

## Overview

The aim of this package is to enable users to write array-based numerical programs
in Python and easily swap in different numerical backends.

The intended use is as follows:

```python
from arraybackend import ArrayBackendCPU, ArrayBackendGPU

# make array on CPU (uses numpy)
ab = ArrayBackendCPU()
arr = ab.array([1, 2, 3])

# make array on NVIDIA GPU (uses cupy)
ab = ArrayBackendGPU()
arr = ab.array([1, 2, 3])
```
