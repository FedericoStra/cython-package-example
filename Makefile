.PHONY: build dist redist install install-from-source clean uninstall

build:
	CYTHONIZE=1 ./setup.py build

dist:
	CYTHONIZE=1 ./setup.py sdist bdist_wheel

redist: clean dist

install:
	CYTHONIZE=1 pip install --user .

install-from-source: dist
	pip install --user dist/cython-package-example-0.1.2.tar.gz

clean:
	$(RM) -r build dist
	$(RM) -r src/cypack/{utils.c,answer.c} src/cypack/sub/wrong.c
	git clean -fdX

uninstall:
	pip uninstall cython-package-example
