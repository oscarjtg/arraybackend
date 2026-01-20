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

## Installation instructions

Clone this repository into the user `site-packages` directory of your Python installation.

This directory can be found by running

```bash
python -m site --user-site
```

Then install the package locally. 
If you wish to execute on NVIDIA GPUs, you must select an optional dependency depending on your CUDA version: 

Optional dependency | CUDA Version
------------------
`[cuda12]` | 12.x
`[cuda13]` | 13.x

The `bash` script below creates and activates a virtual environment called `myenv`, 
clones this repository into the Python user site-packages directory, 
and installs the package and its dependencies into `myenv` for a device with CUDA Version 12.

```bash
python -m venv myenv
source myenv/bin/activate
cd `python -m site --user-site`
git clone https://github.com/oscarjtg/arraybackend.git
cd arraybackend
pip install -e .[cuda12]
