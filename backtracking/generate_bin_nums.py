import itertools

def generate(n: int = 8) -> list[bytes]:
    return [b''.join(bits) for bits in itertools.product([b'0', b'1'], repeat=n)]
