FROM mcr.microsoft.com/playwright/python:v1.23.0-focal

#FROM python:3.8.7

RUN pip install --upgrade pip
RUN pip -V

RUN git clone https://github.com/lincolnsmithy/vericol.git

RUN pip install --root-user-action=ignore pytest
RUN pip install pytest-html
RUN pip install pytest-repeat
RUN pip install Faker
RUN pip install pandas
RUN pip install openpyxl
ENV USERNAME=john.raymond
ENV PW=vericol1
ENV PYTEST_BASE_URL=https://demo.vericol.com/
ENV chrometrace=NO


RUN pytest /vericol/vericobvt.py --count=1 --html=/var/log/testreport.html
RUN pwd
RUN ls -la
RUN ls -la /vericol









