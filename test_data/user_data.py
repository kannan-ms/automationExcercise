import os


class UserData:
    VALID_EMAIL = os.getenv("AE_VALID_EMAIL", "")
    VALID_PASSWORD = os.getenv("AE_VALID_PASSWORD", "")
    INVALID_EMAIL = "wronguser@test.com"
    INVALID_PASSWORD = "wrongpassword"


def get_valid_login_credentials():
    email = UserData.VALID_EMAIL.strip()
    password = UserData.VALID_PASSWORD.strip()

    if not email or not password:
        raise AssertionError(
            "Set AE_VALID_EMAIL and AE_VALID_PASSWORD environment variables to run valid login/logout tests."
        )

    return email, password
