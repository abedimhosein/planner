class HandledError(Exception):
    pass


class InvalidInputError(Exception):
    @staticmethod
    def message():
        return "حداقل یکی از ورودی‌ها نادرست است"
