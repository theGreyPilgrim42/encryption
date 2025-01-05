import logging
import timeit

_logger = logging.getLogger(__name__)


def encrypt(message: str) -> str | bool:
    # Check if the message is alphabetical
    if not isinstance(message, str):
        _logger.error('Message to be encrypted must be a string')
        return False

    result = "".join([_lookup(letter) for letter in message])

    return result


def _lookup(char: str) -> str:
    _LOOKUP_TABLE = {
     'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
     'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
     'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
     'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
     'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
     'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
     'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H',
     'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'
    }
    if char in _LOOKUP_TABLE:
        return _LOOKUP_TABLE[char]

    return char


if __name__ == '__main__':
    _runs = 10_000
    avg_execution_time = timeit.timeit(lambda: encrypt("Hello World!"), number=_runs)
    print(f"Average execution time: {avg_execution_time / _runs} seconds")
