Docker — это приложение, которое упрощает управление процессами приложения в контейнерах * *. Контейнеры позволяют запускать приложения в процессах с изолированием ресурсов. Они подобны виртуальным машинам, но являются при этом более портируемыми, менее требовательны к ресурсам, и больше зависят от операционной системы машины-хоста.

## Установка в систему

    sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

## Копируем ключ GPG официального репозитория Docker.

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

## Добавляем репозиторий Docker в список источников пакетов APT:

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

## Установка.

    sudo apt update

    sudo apt install docker-ce

Теперь Docker установлен, демон запущен, и процесс будет запускаться при загрузке системы.  Убедимся, что процесс запущен:

    sudo systemctl status docker


При установке Docker мы получаем не только сервис (демон) Docker, но и утилиту командной строки docker или клиент Docker. 


Чтобы не вводить sudo каждый раз при запуске команды docker, добавьте имя своего пользователя в группу docker:

    sudo usermod -aG docker ${USER}

Для применения этих изменений в составе группы необходимо разлогиниться и снова залогиниться на сервере или задать следующую команду:

    su - ${USER}

Команда docker позволяет использовать различные опции, команды с аргументами. Синтаксис выглядит следующим образом:

    docker [option] [command] [arguments]

## Установка docker-compose.

    sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose

В Docker есть две важные концепции: образы (images) и контейнеры (containers).

Image: список инструкций для всех программных пакетов в ваших проектах


Другими словами, образ (image) описывает, что произойдет, а контейнер (container) – это то, что фактически выполняется.


Container: экземпляр образа во время выполнения

## Нужно создать Dockerfile,  Python dependencies file, и docker-compose.yml

Dockerfile - определяет и создает образ приложения перечислением команд установки нужного ПО.

Потом этот образ будет запущен внутри контейнера.

Создадим файл в каталоге dj_prj.

    FROM python:3
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /app
    WORKDIR /app
    COPY requirements.txt /app
    RUN pip install -r requirements.txt
    COPY . /app/

Мы начинаем создавать образ (FROM python:3) на основе родительского [тут](https://hub.docker.com/r/library/python/tags/3/)

Далее мы создаем новый каталог внутри контейнера, устанавливаем зависимости и копируем в него код проекта бекенда.

Создаем docker-compose.yml в корне от куда будем запускать docker-compose up. В нем будем описывать сервисы, запущенные нашим приложением.

Так же в этом файле определяются порты, на которых запускаются сервисы и на которые они передаются.

docker-compose.yml


    version: '3.5'

    services:
    django:
        build: ./backend/dj_prj
        command: python manage.py runserver 0.0.0.0:8000
        ports:
            - "8000:8000"
        watch: 
            - *.py

Пытаемся собрать образ.

    docker-compose run web


**ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?**

Нужно запускать из под sudo.

Запуск.

    docker-compose up

Привяжем контейнер к папке с проектом без копирования его во внутрь контейнера.

Dockerfile

    FROM python:3
    ENV PYTHONUNBUFFERED 1
    ADD requirements.txt requirements.txt
    RUN pip install -r requirements.txt
    WORKDIR /backend/dj_prj

docker-compose.yml

    services:
    django:
        build: ./backend/dj_prj
        command: python ./backend/dj_prj/manage.py runserver 0.0.0.0:8000
        ports:
        - "8000:8000"
        volumes:
        - .:/backend/dj_prj
