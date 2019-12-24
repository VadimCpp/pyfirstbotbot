# pyfirstbotbot

> Telegram bot: [https://t.me/pyfirstbotbot](https://t.me/pyfirstbotbot)

This is the starter template for other bots built with python

## Инструкция

Пошаговая инструкция находится:
[frontend-basics.blogspot.com/2019/09/py-first-bot.html](https://frontend-basics.blogspot.com/2019/09/py-first-bot.html)

## Настройка IDE

[Ссылка на скачивание PyCharm.][pycharm_download]
Можно использовать как Community, так и триал Professional.
Professional можно получить на год для учебных целей.
Если не уложитесь в 30 дней, есть возможность сбрасывать триал.


Для форматирования кода использовать комбинацию Ctrl+Alt+l (l == L). 
Не требует настройки.
Использовать для каждого файла по отдельности.
**Перед коммитом/пушем форматируйте код.**

## Инструкция для запуска бота на локальном компьютере

Откройте командную строку и перейдите в папку с исходниками бота. Если вы ещё не скачивали исходники, сделать это и перейти в соответствующую папку можно с помощью следующих команд:
```
git clone https://github.com/VadimCpp/pyfirstbotbot.git
cd pyfirstbotbot
```

Для работы бота необходимы модули, прописанные в файле `requirements.txt`. Для их установки воспользуйтесь следующей командой:
```
pip install -r requirements.txt
```

В папке с исходниками необходимо создать текстовый файл `.env` со следующим содержанием:
```
BOT_TOKEN=YOUR_BOT_TOKEN
MODE=debug
```
Вместо `YOUR_BOT_TOKEN` вставьте токен для бота.

И, наконец, можно запустить бота.
```
python bot.py
```

**Внимание! Если ваш локальный компьютер расположен на территории Российской Федерации, то, скорее всего, боту
соединиться с telegram.org не получится. Для работы бота воспользуйтесь каким-нибудь приложением VPN.**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
[pycharm_download]:<https://www.jetbrains.com/pycharm/download/>
