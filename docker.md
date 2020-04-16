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


## Нужно создать Dockerfile,  Python dependencies file, и docker-compose.yml

Dockerfile - определяет и создает образ приложения перечислением команд установки нужного ПО.

Потом этот образ будет запущен внутри контейнера.

    FROM python:3
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /docker-img
    WORKDIR /docker-img
    COPY requirements.txt /docker-img/
    RUN pip install -r requirements.txt
    COPY . /docker-img/

Мы начинаем создавать образ (FROM python:3) на основе родительского [тут](https://hub.docker.com/r/library/python/tags/3/)

Создаем docker-compose.yml в корне.

docker-compose.yml