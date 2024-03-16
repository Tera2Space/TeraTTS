text = "Привет, мир!"

from TeraTTS import TTS

# Опционально: Предобработка текста (улучшает качество)
from ruaccent import RUAccent
accentizer = RUAccent()

# Загрузка моделей акцентуации и словарей
accentizer.load(omograph_model_size='turbo', use_dictionary=True)

# Обработка текста с учетом ударений и буквы ё
text = accentizer.process_all(text)
print(f"Текст с ударениями и ё: {text}")


# Примечание: Вы можете найти все модели по адресу https://huggingface.co/TeraTTS, включая модель GLADOS
tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=1.0, tokenizer_load_dict=True) # Вы можете настроить 'add_time_to_end' для продолжительности аудио, 'tokenizer_load_dict' можно отключить если используете RUAccent


# 'length_scale' можно использовать для замедления аудио для лучшего звучания (по умолчанию 1.1, указано здесь для примера)
audio = tts(text, lenght_scale=1.1)  # Создать аудио. Можно добавить ударения, используя '+'
tts.play_audio(audio)  # Воспроизвести созданное аудио
tts.save_wav(audio, "./test.wav")  # Сохранить аудио в файл


# Создать аудио и сразу его воспроизвести
tts(text, play=True, lenght_scale=1.1)
