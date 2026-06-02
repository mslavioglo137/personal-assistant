def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError as error:
            return str(error)

        except KeyError:
            return "Contact not found."

        except IndexError:
            return "Enter the argument for the command."

    return inner