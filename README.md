# Russian TTS inference
# Установка
Вы можете установить пакет с помощью pip:
```
pip install TeraTTS
```
Также вы можете установить используя Git:
```
pip install -e git+https://github.com/Tera2Space/RUTTS#egg=TeraTTS
```
# Ошибки
1)Если на Windows у вас **ошибка при установке**,нужно просто **скачать Visual Studio [здесь](https://visualstudio.microsoft.com/ru/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)** и при установке выбрать галочку около **Разработка классических приложений на С++**

2)Если **после установки не работает** что-то, **убедитесь что модуль скачан последней версии**(удалить и скачать) и **так же что названия моделей есть на** https://huggingface.co/TeraTTS

3)Если ничего не помогло **обратитесь за помощью в https://t.me/teraspace_chat**
# Использование

```python  
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

```
