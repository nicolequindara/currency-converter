FROM python:3.12 AS python-base

ENV PIP_ROOT_USER_ACTION=ignore

COPY pyproject.toml .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 

COPY . .

RUN pip install fastapi[standard]

EXPOSE 8000