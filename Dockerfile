FROM binxio/gcp-get-secret:0.4.1
#FROM mcr.microsoft.com/playwright/python:v1.23.0-focal
FROM alpine:3.6
#FROM python:3.8.7

FROM binxio/gcp-get-secret:0.4.1




COPY --from=0 /gcp-get-secret /usr/local/bin/

#RUN pip install --upgrade pip
#RUN pip -V

#RUN git clone https://github.com/lincolnsmithy/vericol.git

#RUN pip install --root-user-action=ignore pytest
#RUN pip install pytest-html
#RUN pip install pytest-repeat 
#RUN pip install Faker
#RUN pip install pandas
#RUN pip install openpyxl
ENV USERNAME=me
ENV PGPASSWORD=gcp:///projects/180640329096/secrets/user_pass/version/1
#ENV PYTEST_BASE_URL=me
#ENV chrometrace=NO

ENTRYPOINT [ "/usr/local/bin/gcp-get-secret", "--use-default-credentials"]
CMD [ "/bin/bash", "-c", "echo $PGPASSWORD"]
echo $PGPASSWORD
echo FUCKOFF
#RUN echo $MYSECRET
#RUN pytest -v /vericol/vericobvt.py --count=1 --html=/vericol/testreport.html









