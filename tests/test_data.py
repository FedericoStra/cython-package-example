from subprocess import check_output
from cypack.answer import zen_hash


def test_zen_hash():
    md5sum = check_output(["md5sum", "src/cypack/data/zen.txt"]).split(maxsplit=1)[0]
    assert md5sum == zen_hash().encode("ascii")
