from setuptools import Extension
from Cython.Build import cythonize


extensions = [
    Extension("cypack.utils", ["src/cypack/utils.pyx"]),
    Extension("cypack.answer", ["src/cypack/answer.pyx"]),
    Extension("cypack.fibonacci", ["src/cypack/fibonacci.pyx"]),
    Extension(
        "cypack.sub.wrong", ["src/cypack/sub/wrong.pyx", "src/cypack/sub/helper.c"]
    ),
]

compiler_directives = {"language_level": 3, "embedsignature": True}


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(
                extensions, compiler_directives=compiler_directives
            ),
        }
    )
