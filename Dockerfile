FROM debian:buster

RUN apt update;

RUN apt install -y git

RUN apt install -y python3

RUN apt install -y python3-pip

RUN apt install -y libffi-dev

RUN mkdir -p /botrdel

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

COPY run.sh /tmp/run.sh
COPY botrdel.py /botrdel/botrdel.py
COPY chaine_de_mot_bordel /botrdel/chaine_de_mot_bordel

ENTRYPOINT ["/tmp/run.sh"]
