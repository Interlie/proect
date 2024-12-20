BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class Base64Encoder:
    def __init__(self):
        self.alphabet = BASE64_ALPHABET

    def encode(self, input_string):
        """Кодирует строку в base64."""
        # Преобразуем строку в бинарный формат
        binary_string = ''.join(format(ord(char), '08b') for char in input_string)

        # Добавляем нули, если длина не кратна 6
        while len(binary_string) % 6 != 0:
            binary_string += '0'

        # Кодируем бинарный формат в base64
        encoded_string = ''
        for i in range(0, len(binary_string), 6):
            byte = binary_string[i:i+6]
            index = int(byte, 2)
            encoded_string += self.alphabet[index]

        # Добавляем символы '=' для выравнивания
        padding_length = (4 - len(encoded_string) % 4) % 4
        encoded_string += '=' * padding_length

        return encoded_string

# Пример использования
base64_encoded = Base64Encoder()

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


# Пример использования
base64_decoded = Base64Decoder()
basee64_encoded = Base64Encoder()


print ('ввести сообщение - 1, ввести файл -2')
fd = input()
if (fd == '1'):
    print('введите сообщение')
    input_message = input()

#-------------------------------------------------------------------- здесь ошибка
elif (fd=='2'):
    print ('введите путь документа без кавычек')
    path = input()
    with open(path, 'r') as file:
        input_message = file.read()




print('выбирете действие: кодировать -1, декодировать -2')
f = input()
if (f == '2'):
    decoded_message = base64_decoded.decode(input_message)
    print(f"Input: {input_message}")
    print(f"Decoded: {decoded_message}")


elif (f=='1'):
    encoded_message = base64_encoded.encode(input_message)
    print(f"Input: {input_message}")
    print(f"Encoded: {encoded_message}")
