FROM debian:buster

RUN apt update;

RUN apt install -y git

RUN mkdir -p /botrdel

COPY run.sh /tmp/run.sh
COPY botrdel.py /botrdel/botrdel.py
COPY chaine_de_mot_bordel /botrdel/chaine_de_mot_bordel

ENTRYPOINT ["/tmp/run.sh"]
