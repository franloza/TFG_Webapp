FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN mkdir -p /root/app/
RUN mkdir -p /root/logs
WORKDIR /root/app/
COPY ./Pipfile* ./
ENV PIPENV_MAX_RETRIES=3
ENV PIPENV_TIMEOUT=600
RUN pipenv install --system --deploy --ignore-pipfile --dev

COPY src .
COPY ./docker-entrypoint.sh .
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
