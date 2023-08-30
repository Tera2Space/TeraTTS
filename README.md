# Russian TTS inference
# Установка
**1)Установка пакета:**

  **a) скачать из pypi: pip install RUTTS**
  
  **b) из гита (нужен установленный гит) pip install -e git+https://github.com/Tera2Space/RUTTS#egg=RUTTS**
# Ошибки
1)Если на винде у вас **ошибка при установке**,нужно просто **скачать Visual Studio [здесь](https://visualstudio.microsoft.com/ru/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)** и при установке выбрать галочку около **Разработка классических приложений на С++**

2)Если **после установки не работает** что-то, **убедитесь что модуль скачан последней версии**(удалить и скачать) и **так же что названия моделей есть на** https://huggingface.co/TeraTTS
# Использование

```python  
  from RUTTS import TTS

  #! Cоздать модель по имени
  # P.S все модели https://huggingface.co/TeraTTS P.S там есть модель для GLADOS
  tts = TTS("TeraTTS/natasha-g2p-vits") # Можно передать параметр add_time_to_end (по умолчанию = 0.8) это кол-во добавленных секунд в аудио для хорошего звучания

  text = "Привет мир!"
  print(f"Текст: {text}")

  #! Предобработка текста (это по желанию, но сильно улучшает качество!)
  from RUTTS.ruaccent import RUAccent #https://github.com/Den4ikAI/ruaccent
  accentizer = RUAccent(workdir="./model")#allow_cuda=False что бы отключить использование видеокарты
  # load(omograph_model_size='medium', dict_load_startup=False): 
  # Загрузка моделей и словарей. На данные момент доступны две модели: medium (рекомендуется к использованию) и small. 
  # Переменная dict_load_startup отвечает за загрузку всего словаря (требуется больше ОЗУ), 
  # либо во время работы для необходимых слов (экономит ОЗУ, но требует быстрые ЖД и работает медленее)
  accentizer.load(omograph_model_size='medium', dict_load_startup=False)
  text = accentizer.process_all(text)
  print(f"Текст с ударениями и ё: {text}")

  #! Синтез
  #lenght_scale - замедлить аудио для хорошего звучания, параметр по умолчанию передается как 1.2, указан для примера
  audio = tts(text, lenght_scale=1.2) # Создать аудио. Можно ставить ударения используя +
  tts.play_audio(audio) # Проиграть созданное аудио
  tts.save_wav(audio, "./test.wav") # Сохранить аудио

  tts(text, play=True, lenght_scale=1.2) # Создать аудио и сразу проиграть его

```
