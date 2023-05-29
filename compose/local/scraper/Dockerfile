FROM python:3.11.3-slim-buster
LABEL maintainer="Sbtah"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG DEV=false

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Aditional dependecies
  && apt-get install -y procps \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./scraper/requirements.txt /requirements.txt
COPY ./scraper/requirements.dev.txt /requirements.dev.txt
RUN pip install -r /requirements.txt && \
  if [ $DEV = "true" ]; \
  then pip install -r requirements.dev.txt ; \
  fi

COPY ./compose/local/scraper/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/scraper/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# WORKER
COPY ./compose/local/scraper/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/scraper/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/scraper/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /scraper

ENTRYPOINT ["/entrypoint"]