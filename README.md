# Russian TTS inference
# Установка
Вы можете установить пакет с помощью pip:
```
pip install RUTTS
```
Также вы можете установить используя Git:
```
pip install -e git+https://github.com/Tera2Space/RUTTS#egg=RUTTS
```
# Ошибки
1)Если на Windows у вас **ошибка при установке**,нужно просто **скачать Visual Studio [здесь](https://visualstudio.microsoft.com/ru/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)** и при установке выбрать галочку около **Разработка классических приложений на С++**

2)Если **после установки не работает** что-то, **убедитесь что модуль скачан последней версии**(удалить и скачать) и **так же что названия моделей есть на** https://huggingface.co/TeraTTS
# Использование

```python  
from RUTTS import TTS

# Создание модели TTS с указанным именем
# Примечание: Вы можете найти все модели по адресу https://huggingface.co/TeraTTS, включая модель GLADOS
tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=0.8)  # Вы можете настроить 'add_time_to_end' для продолжительности аудио

text = "Привет, мир!"
# Опционально: Предобработка текста (улучшает качество)
from ruaccent import RUAccent
accentizer = RUAccent(workdir="./model")

# Загрузка моделей акцентуации и словарей
# Доступны две модели: 'medium' (рекомендуется) и 'small'.
# Переменная 'dict_load_startup' управляет загрузкой словаря при запуске (больше памяти) или загрузкой его по мере необходимости во время выполнения (экономия памяти, но медленнее).
# Переменная disable_accent_dict отключает использование словаря (все ударения расставляет нейросеть). Данная функция экономит ОЗУ, по скорости работы сопоставима со всем словарём в ОЗУ.
accentizer.load(omograph_model_size='medium', dict_load_startup=False)

# Обработка текста с учетом ударений и буквы ё
text = accentizer.process_all(text)
print(f"Текст с ударениями и ё: {text}")

# Синтез речи
# 'length_scale' можно использовать для замедления аудио для лучшего звучания (по умолчанию 1.2, указано здесь для примера)
audio = tts(text, length_scale=1.2)  # Создать аудио. Можно добавить ударения, используя '+'
tts.play_audio(audio)  # Воспроизвести созданное аудио
tts.save_wav(audio, "./test.wav")  # Сохранить аудио в файл

# Создать аудио и сразу его воспроизвести
tts(text, play=True, length_scale=1.2)

```
