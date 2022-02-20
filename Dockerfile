FROM python:3

ENV BASE_DIR=/deals

RUN mkdir -p $BASE_DIR
RUN mkdir -p $BASE_DIR/static

WORKDIR $BASE_DIR

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $BASE_DIR
RUN pip install -r requirements.txt

