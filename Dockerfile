FROM mcr.microsoft.com/playwright/python:v1.23.0-focal

#FROM python:3.8.7

#WORKDIR /root

RUN pip3 -V

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser

RUN git clone https://github.com/lincolnsmithy/vericol.git
RUN pip3 install pytest
RUN pip3 install pytest-html
RUN pip3 install pytest-repeat
RUN pip3 install Faker
RUN pip3 install pandas

ENV USERNAME=john.raymond
ENV PW=vericol1
ENV PYTEST_BASE_URL=https://demo.vericol.com/
ENV chrometrace=NO


RUN pytest /vericol/vericobvt.py --count=1 --html=/vericol/testreport.html
RUN pwd
RUN ls -la /vericol
RUN ls -la /

RUN cat /vericol/testreport.html






