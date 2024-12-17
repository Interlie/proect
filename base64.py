import base64

def encode_base64(message):
    """Кодирует сообщение в формат Base64.

    Args:
        message: Сообщение для кодирования (строка).

    Returns:
        Закодированное сообщение в виде строки, или None в случае ошибки.
    """
    try:
        message_bytes = message.encode('utf-8')  # Кодируем строку в байты (utf-8)
        base64_bytes = base64.b64encode(message_bytes)  # Кодируем байты в base64
        base64_message = base64_bytes.decode('utf-8') # декодируем байты в строку
        return base64_message
    except Exception as e:
        print(f"Ошибка при кодировании: {e}")
        return None


def decode_base64(base64_message):
    """Декодирует сообщение из формата Base64.

    Args:
        base64_message: Сообщение в формате Base64 (строка).

    Returns:
        Декодированное сообщение в виде строки, или None в случае ошибки.
    """
    try:
        base64_bytes = base64_message.encode('utf-8') # кодируем строку в байты
        message_bytes = base64.b64decode(base64_bytes) # Декодируем base64 в байты
        message = message_bytes.decode('utf-8')  # Декодируем байты в строку (utf-8)
        return message
    except Exception as e:
        print(f"Ошибка при декодировании: {e}")
        return None


if __name__ == "__main__":
    while True:
      print("\nМеню:")
      print("1. Закодировать сообщение в Base64")
      print("2. Декодировать сообщение из Base64")
      print("3. Выход")

      choice = input("Выберите действие: ")

      if choice == "1":
          message = input("Введите сообщение для кодирования: ")
          encoded_message = encode_base64(message)
          if encoded_message:
              print("Закодированное сообщение:", encoded_message)
      elif choice == "2":
          base64_message = input("Введите сообщение для декодирования: ")
          decoded_message = decode_base64(base64_message)
          if decoded_message:
             print("Декодированное сообщение:", decoded_message)
      elif choice == "3":
          print("Программа завершена.")
          break
      else:
          print("Некорректный ввод. Пожалуйста, выберите действие из меню.")