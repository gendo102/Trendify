FROM centos/python-27-centos7

WORKDIR /home/cuadmin/Trendify/app
USER root
COPY requirements.txt ./
COPY Trendify.py ./

RUN yum -y install epel-release
RUN yum -y install python-devel
RUN yum -y install python-pip
ENV LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./Trendify.py" ]
