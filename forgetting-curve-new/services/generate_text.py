import string
import random



class GenerateText:

    @staticmethod
    def generate_char(num: int=random.randint(1, 26)) -> str:
        """
        Генерирует строчку из случайных английских символов, нужное количество символов
        передается в параметр 'num'
        """
        final_str = ''

        for i in range(num):
            rnd = random.randint(1, 26)
            final_str = final_str + string.ascii_lowercase[rnd-1]

        return final_str


    @staticmethod
    def get_invalid_characters() -> list:
        """
        Возвращает лист (список) со знаками препинания. (Для проверки полей на запрещенные символы)
        """
        INVALID_CHARACTERS = list((string.punctuation.replace("-", "").replace("_", "")))
        result = [char + 'test' for char in INVALID_CHARACTERS]
        return result


    @staticmethod
    def get_invalid_email() -> list:
        """
        Возвращает список невалидных email
        """
        emails_structure = [
                    'invalid-email',
                    'test@.com',
                    'test@example..com',
                    'test.@example.com',
                    'test@example.com.',
                    'test@example',
                    'test@@example.com',
                    'test@example..co.uk',
                    'test example@com',
                    '"test with space"@example.com'
        ]
        lst = [GenerateText.generate_char(random.randint(1,16)) + email for email in emails_structure]
        return lst


    @staticmethod
    def get_invalid_password() -> list:
        """
        Возвращает список невалидных паролей, если условие:
        - Имеет длину не менее 8 символов
        - Как минимум одна заглавная английская буква
        - Как минимум одна строчная английская буква
        - Как минимум одна цифра
        - Как минимум один специальный символ
        """
        return [
            "short1!",  # Слишком короткий
            "TOOLONG",  # Только заглавные, нет цифры, нет спецсимвола
            "alllowercase2*",  # Только строчные, должен быть 8+ символов
            "NoLet1!",  # Нет букв, должен быть 8+ символов
            "NoNumbrAZ",  # Нет цифр, должен быть 8+ символов
            "NoSymbolA12",  # Нет спецсимволов, должен быть 8+ символов
            "ShrtA1!",  # Слишком короткий, 7 символов
            "VeryLongPasswordWithoutNumbers!@#",  # Слишком длинный, без цифр
            "abcdefgh1234567890",  # Слишком длинный, нет заглавных и спецсимволов
            "Loooooooooooooooooooooooongpassword1",  # Слишком длинный, нет спецсимвола
        ]


