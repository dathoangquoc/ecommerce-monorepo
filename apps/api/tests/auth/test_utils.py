from src.auth.utils import create_access_token, decode_token, hash_password, verify_password


def test_hash_password():
    hashed = hash_password("mypassword")
    assert len(hashed) == 256;


def test_verify_password():
    assert verify_password(plain="mypassword", hashed=hash_password("mypassword"))

