BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class Base64Encoder:
    def __init__(self):
        self.alphabet = BASE64_ALPHABET

    def encode(self, input_string):
        """Кодирует строку в base64."""
        binary_string = ''.join([format(ord(char), '08b') for char in input_string])

        # Добавляем нули, чтобы длина была кратна 6
        padding_length = (6 - len(binary_string) % 6) % 6
        binary_string += '0' * padding_length

        # Разбиваем на группы по 6 бит и преобразуем в base64
        base64_string = ''
        for i in range(0, len(binary_string), 6):
            six_bit_group = binary_string[i:i + 6]
            base64_index = int(six_bit_group, 2)
            base64_string += self.alphabet[base64_index]

        # Добавляем символы '=' для выравнивания
        padding = '=' * (len(input_string) % 3)
        return base64_string + padding


class Base64Decoder:
    def __init__(self):
        self.alphabet = BASE64_ALPHABET

    def decode(self, encoded_string):
        """Декодирует строку из base64."""
        # Убираем символы '=', используемые для выравнивания
        padding_length = encoded_string.count('=')
        encoded_string = encoded_string.rstrip('=')

        # Преобразуем символы base64 в бинарный формат
        binary_string = ''
        for char in encoded_string:
            if char in self.alphabet:
                base64_index = self.alphabet.index(char)
                binary_string += format(base64_index, '06b')

        # Убираем добавленные нули
        if padding_length:
            binary_string = binary_string[:-padding_length * 2]

        # Преобразуем бинарный формат обратно в текст
        decoded_string = ''
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i + 8]
            decoded_string += chr(int(byte, 2))

        return decoded_string


class Base64Utility(Base64Encoder, Base64Decoder):
    def __init__(self):
        Base64Encoder.__init__(self)
        Base64Decoder.__init__(self)


# Пример использования
base64_util = Base64Utility()
original_message = input()
encoded_message = base64_util.encode(original_message)
decoded_message = base64_util.decode(encoded_message)

print(f"Original: {original_message}")
print(f"Encoded: {encoded_message}")
print(f"Decoded: {decoded_message}")
