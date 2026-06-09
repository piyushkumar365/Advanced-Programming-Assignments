import re
import pytest

# 1. CUSTOM EXCEPTIONS

class InvalidEmailError(ValueError):
    """
    Raised when email validation fails.
    Inherits from ValueError because input value is invalid.
    """
    pass


class UnderageError(ValueError):
    """
    Raised when user's age is below minimum age requirement.
    """
    pass


# 2. REGISTRATION SERVICE

class RegistrationService:

    def register_user(self, email: str, age: int) -> bool:

        # INTERNAL ASSERTIONS (STATE INVARIANTS)

        assert isinstance(age, int), "Age must always remain integer type"

        # EMAIL VALIDATION

        # Null check
        if email is None:
            raise InvalidEmailError(
                "Email cannot be None."
            )

        # Empty string check
        if email.strip() == "":
            raise InvalidEmailError(
                "Email cannot be empty."
            )

        # Regex email validation
        email_pattern =r'^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z-]+\.[A-Za-z]{2,}$'
        if not re.match(email_pattern, email):
            raise InvalidEmailError(
                f"'{email}' is not a valid email format."
            )

        # AGE VALIDATION

        if age < 18:
            raise UnderageError(
                f"Registration denied. User age {age} is below 18."
            )

        # Registration successful      
        return True


# 3. MAIN DRIVER PROGRAM

def main():

    service = RegistrationService()

    try:
        # User input
        email = input("Enter Email: ")

        age_input = input("Enter Age: ")
        age = int(age_input)

        # Registration attempt
        result = service.register_user(email, age)

        if result:
            print("\nRegistration Successful!")

    except InvalidEmailError as e:
        print(f"\nInvalidEmailError: {e}")

    except UnderageError as e:
        print(f"\nUnderageError: {e}")

    except ValueError:
        print("\nAge must be an integer.")

    except AssertionError as e:
        print(f"\nAssertionError: {e}")

    finally:
        print("Program execution completed.")


# 4. PYTEST FIXTURE

@pytest.fixture
def registration_service():
    """
    Shared fixture for creating RegistrationService object.
    """
    return RegistrationService()


# 5. PYTEST TEST CASES

def test_successful_registration(registration_service):

    result = registration_service.register_user(
        "test@gmail.com",
        21
    )

    assert result is True

def test_invalid_email_format(registration_service):

    with pytest.raises(InvalidEmailError):

        registration_service.register_user(
            "invalid-email",
            25
        )


def test_empty_email(registration_service):

    with pytest.raises(InvalidEmailError):

        registration_service.register_user(
            "",
            25
        )


def test_none_email(registration_service):

    with pytest.raises(InvalidEmailError):

        registration_service.register_user(
            None,
            25
        )


def test_underage_user(registration_service):

    with pytest.raises(UnderageError):

        registration_service.register_user(
            "user@gmail.com",
            16
        )


def test_assertion_for_age_type(registration_service):

    with pytest.raises(AssertionError):

        registration_service.register_user(
            "user@gmail.com",
            "twenty"
        )


# 6. ENTRY POINT

if __name__ == "__main__":
    main()