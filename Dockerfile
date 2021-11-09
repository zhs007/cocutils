FROM python:3.8-buster

LABEL writer="zerrozhao@gmail.com"

WORKDIR /src/cocutils

COPY . /src/cocutils/

RUN pip install -r requirements.env.txt
RUN pip install -r requirements.txt

CMD ["python", "main.py"]