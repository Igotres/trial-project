# Amazing Hunting

Amazing Hunting - это веб-приложение, созданное с использованием Django 4.2.6.

## Установка

1. Клонируйте репозиторий на свой локальный компьютер.
2. Установите зависимости, используя pip:

```bash
pip install -r requirements.txt

Настройка
Настройки проекта находятся в файле settings.py. Вот некоторые из ключевых параметров, которые вам, возможно, придется настроить:

SECRET_KEY: Это секретный ключ Django, который используется для предоставления криптографической подписи. Никогда не делайте его общедоступным!
DEBUG: Этот параметр определяет, будет ли включен режим отладки. Не включайте его в производственной среде!
ALLOWED_HOSTS: Список хостов, которым разрешено обслуживать этот проект.
DATABASES: Настройки базы данных для проекта.
Запуск
Чтобы запустить проект, используйте команду:

python manage.py runserver
