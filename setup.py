#!/usr/bin/python3

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os.path
import os


def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in (".pyx", ".py"):
                if extension.language == "c++":
                    ext = ".cpp"
                else:
                    ext = ".c"
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions


extensions = [
    Extension("cypack.answer", ["src/cypack/answer.pyx"]),
    Extension("cypack.utils", ["src/cypack/utils.pyx"]),
    Extension(
        "cypack.sub.wrong", ["src/cypack/sub/wrong.pyx", "src/cypack/sub/helper.c"]
    ),
]

USE_CYTHON = bool(int(os.getenv("USE_CYTHON", 0)))

if USE_CYTHON:
    extensions = cythonize(
        extensions, compiler_directives={"language_level": 3, "embedsignature": True}
    )
else:
    extensions = no_cythonize(extensions)


with open("requirements.txt") as fp:
    install_requires = fp.read().strip().split("\n")

with open("requirements-dev.txt") as fp:
    dev_requires = fp.read().strip().split("\n")

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="cython-package-example",
    version="0.1.0",
    description="Example of a package with Cython extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Federico Stra",
    author_email="stra.federico@gmail.com",
    url="",
    project_urls={"Documentation": "", "Code": "", "Issue tracker": ""},
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.pxd", "*.h"], "cypack": ["data/*"]},
    ext_modules=extensions,
    zip_safe=False,
    python_requires=">=3.4",
    # setup_requires=["Cython >= 0.29"],
    extras_require={"dev": dev_requires, "docs": ["sphinx", "sphinx-rtd-theme"]},
)
