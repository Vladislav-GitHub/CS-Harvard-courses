from validator_collection import validators, errors


def main():
    email_address = input("What's your email address? ")
    try:
        email_is_valid = validators.email(email_address)
        print('Valid')
    except (errors.EmptyValueError, errors.InvalidEmailError):
        print('Invalid')
    else:
        pass


if __name__ == '__main__':
    main()