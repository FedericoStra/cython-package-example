.PHONY: build dist install install-from-source clean

build:
	USE_CYTHON=1 ./setup.py build

dist:
	USE_CYTHON=1 ./setup.py sdist bdist_wheel

install:
	USE_CYTHON=1 pip install --user .

install-from-source: dist
	pip install --user dist/cython-package-example-0.1.0.tar.gz

clean:
	$(RM) -r build dist
	$(RM) -r src/cypack/{utils.c,answer.c} src/cypack/sub/wrong.c
	git clean -fdX
