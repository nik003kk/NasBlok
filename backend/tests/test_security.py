"""Enotski testi gesel in JWT zetonov brez potrebe po podatkovni bazi."""
from datetime import datetime, timedelta, timezone

import jwt

from app.config import settings
from app.security import create_access_token, decode_access_token, hash_password, verify_password


def test_hash_password_is_not_plaintext():
    assert hash_password("varnoGeslo123") != "varnoGeslo123"


def test_verify_password_accepts_correct_password():
    hashed = hash_password("varnoGeslo123")
    assert verify_password("varnoGeslo123", hashed)


def test_verify_password_rejects_wrong_password():
    hashed = hash_password("varnoGeslo123")
    assert not verify_password("napacnoGeslo123", hashed)


def test_hash_uses_different_salts():
    assert hash_password("enakoGeslo123") != hash_password("enakoGeslo123")


def test_access_token_roundtrip():
    assert decode_access_token(create_access_token(42)) == 42


def test_invalid_token_is_rejected():
    assert decode_access_token("not.a.jwt") is None


def test_expired_token_is_rejected():
    token = jwt.encode(
        {"sub": "42", "exp": datetime.now(timezone.utc) - timedelta(minutes=1)},
        settings.jwt_secret,
        algorithm="HS256",
    )
    assert decode_access_token(token) is None


def test_token_with_invalid_user_id_is_rejected():
    token = jwt.encode(
        {"sub": "not-a-number", "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
        settings.jwt_secret,
        algorithm="HS256",
    )
    assert decode_access_token(token) is None
