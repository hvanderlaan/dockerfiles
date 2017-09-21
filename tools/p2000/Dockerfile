FROM alpine:latest
LABEL maintainer "Harald van der Laan"

# install requirements from packagemanagement
RUN apk update
RUN apk add python curl

# download pip and install pip
RUN curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
RUN python get-pip.py

# download and install request and bs4 from pip
RUN pip install requests bs4 --upgrade

# deploying localfiles to docker
COPY p2000.py ./p2000.py
COPY p2000.cfg ./p2000.cfg
COPY libp2000 ./libp2000/

# run the script
ENTRYPOINT ["./p2000.py"]
