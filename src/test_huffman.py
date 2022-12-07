"""Test Huffman coding"""

import random
import string
from huffman import Encoding


def test_minimal() -> None:
    """You will want to test more than this..."""
    x = "aabacabaaa"
    enc = Encoding(x)
    assert x == enc.decode(enc.encode(x))

def test_random()-> None:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    x = ''.join(random.choice(alphabet) for i in range(random.randint(0, 500)))
    enc = Encoding(x)
    assert x == enc.decode(enc.encode(x))
