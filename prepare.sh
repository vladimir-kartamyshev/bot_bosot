#!/bin/bash

# Запускать в папке проекта (/opt/soso_bot)
apt-get update
apt install -y python3-pip
apt install -y python3-venv

# создадим виртуальное окружение и установим в него зависимости согласно requirements.txt
python3 -m venv ubuntu_env

source ubuntu_env/bin/activate

pip install -r requirements.txt

deactivate

# дадим право на исполнение скрипта запуска
chmod +x run.sh

# сконфигурируем сервис
ln -s /opt/botbosot/botbosot.service /etc/systemd/system/botbosot.service
chmod 664 /etc/systemd/system/botbosot.service
systemctl daemon-reload

# добавим в автозагрузку
systemctl enable botbosot

systemctl status botbosot