FROM debian:buster

RUN apt update;

RUN apt install -y git python3 python3-pip libffi-dev

RUN mkdir -p /botrdel

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

COPY run.sh /tmp/run.sh
COPY botrdel.py /botrdel/botrdel.py
COPY chaine_de_mot_bordel /botrdel/chaine_de_mot_bordel

ENTRYPOINT ["/tmp/run.sh"]
