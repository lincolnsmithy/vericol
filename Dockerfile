FROM binxio/gcp-get-secret:0.4.1
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
ENV USERNAME=
ENV PW=gcp:///projects/180640329096/secrets/user_pass
ENV PYTEST_BASE_URL
ENV chrometrace=NO

#RUN pytest -v /vericol/vericobvt.py --count=1 --html=/vericol/testreport.html










