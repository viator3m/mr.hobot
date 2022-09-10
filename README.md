### Телеграм-бот [mr. hobot](https://t.me/mr_hobot)

Бот реализован с помощью библиотеки [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

#### Функционал:
- здоровается с пользователем по имени и сразу отправляет фото/гифку с котом
- реализованы две инлайн-кнопки "Еще фото" и "Еще гифку"
- В ответ на любое сообщение пользователя реагирует заранее подготовленным ответом
- В случае недоступности основного API – [The Cat API](https://thecatapi.com/), 
  логирует ошибку и делает запрос на [The Dog API](https://thedogapi.com/)

Деплой бота осуществлен на облачной платформе Heroku.

![example_of_work](https://i.postimg.cc/mDHtjvh4/example-of-work.gif)

#### Запуск бота:
- клонировать репозиторий
```
git clone git@github.com:viator3m/mr.hobot.git
```
- создать виртуальное окружение и установить зависимости
```
python -m venv venv
source venv/Scripts/activate (win)
source venv/Scripts/activate (linux)
pip install -r requirements.txt
```
- создать файл с переменными окружения, ориентируясь на [образец](.env.example)
- запустить исполняемый файл
```
python kittybot.py
```
