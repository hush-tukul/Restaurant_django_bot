FROM python:3.11
ENV BOT_NAME=$BOT_NAME
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"
RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt

COPY . .

#COPY Restaurant_django_bot /usr/src/app/"${BOT_NAME:-tg_bot}"




