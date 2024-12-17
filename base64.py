import base64

class Base64Converter:
    # Класс для кодирования и декодирования сообщений в формате Base64

    def encode(self, message):
        # Кодируем сообщение в формат Base64

        Args:
            message: Сообщение для кодирования (строка).

        Returns:
        try:
            message_bytes = message.encode('utf-8')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('utf-8')
            return base64_message
        except Exception as e:
            print(f"Ошибка при кодировании: {e}")
            return None


    def decode(self, base64_message):
        # Декодируем сообщение из формата Base64.

        Args:
            base64_message: Сообщение в формате Base64 (строка).

        Returns:
        try:
            base64_bytes = base64_message.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception as e:
            print(f"Ошибка при декодировании: {e}")
            return None

def main():
    # Основная функция для работы с классом Base64Converter
    converter = Base64Converter()

    while True:
        print("\nМеню:")
        print("1. Закодировать сообщение в Base64")
        print("2. Декодировать сообщение из Base64")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            message = input("Введите сообщение для кодирования: ")
            encoded_message = converter.encode(message)
            if encoded_message:
                print("Закодированное сообщение:", encoded_message)
        elif choice == "2":
            base64_message = input("Введите сообщение для декодирования: ")
            decoded_message = converter.decode(base64_message)
            if decoded_message:
                print("Декодированное сообщение:", decoded_message)
        elif choice == "3":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
