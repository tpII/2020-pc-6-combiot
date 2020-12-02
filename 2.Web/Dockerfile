FROM python:3.8.6-alpine3.12

ENV VERSION=3.6.3

RUN apk add openjdk8 wget gcc g++ \
    && wget -O /tmp/maven.tar.gz https://apache.dattatec.com/maven/maven-3/3.6.3/binaries/apache-maven-$VERSION-bin.tar.gz \
    && tar -zxvf /tmp/maven.tar.gz -C /etc/ \
    && mv /etc/apache-maven-$VERSION /etc/maven \
    && pip install pyzxing

ENV PATH=/etc/maven/bin:$PATH
