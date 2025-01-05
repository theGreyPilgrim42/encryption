from rot_13.rot_13 import encrypt


def test_encrypt():
    assert encrypt("Hello World!") == "Uryyb Jbeyq!"
    assert encrypt("This is a test.") == "Guvf vf n grfg."


def test_encrypt_with_invalid_input():
    assert encrypt({}) == False
    assert encrypt(123) == False
