from subprocess import check_output
import sys
from cypack.answer import zen_hash


def test_zen_hash():
    if sys.platform.startswith("darwin"):
        md5sum = check_output(["md5",
                               "src/cypack/data/zen.txt"]
                              ).split(b'=')[-1].strip()
    elif sys.platform.startswith("win"):
        md5sum = check_output(["certutil",
                               "-hashfile",
                               r"src\cypack\data\zen.txt",
                               "md5"]).splitlines()[1]
    else:
        md5sum = check_output(["md5sum",
                               "src/cypack/data/zen.txt"]
                              ).split(maxsplit=1)[0]
    assert md5sum == zen_hash().encode("ascii")
