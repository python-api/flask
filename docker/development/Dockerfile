ARG BUILDPLATFORM

FROM --platform=$BUILDPLATFORM python:3.10 AS builder

WORKDIR /app
COPY requirements.txt /code
RUN pip install --upgrade pip

COPY . .
EXPOSE 8000

CMD ["flask", "run"]