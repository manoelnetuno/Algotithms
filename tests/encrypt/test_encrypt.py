from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    valid_message = "message"
    invalid_message = 123
    invalid_key = "invalid_key"

    key_too_large = 10
    key_odd = 3
    key_even = 4
    key_greater_than_length = 9

    expec_rever_message = valid_message[::-1]
    expec_odd_key_result = "sem_egas" 
    expec_even_key_result = "ega_ssem" 

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(valid_message, invalid_key)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, key_odd)

    assert encrypt_message(valid_message, key_too_large) == expec_rever_message

    result = encrypt_message(valid_message, key_odd)
    assert result == expec_odd_key_result

    result = encrypt_message(valid_message, key_even)
    assert result == expec_even_key_result

    result = encrypt_message(valid_message, key_greater_than_length)
    assert result == expec_rever_message
