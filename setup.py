import os

from setuptools import setup

if os.environ.get("USE_MYPYC") == "1":
    import glob
    from mypyc.build import mypycify
    files = glob.glob("src/**/*.py", recursive=True)
    ext_modules = mypycify(files)
else:
    ext_modules = []

setup(ext_modules=ext_modules)
