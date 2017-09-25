# containerized version of ikea-smartlight
FROM debian:stretch
LABEL maintainer "Harald van der Laan"

ENV BuildDeps "git build-essential automake libtool"

# installing required tools
RUN apt-get -qq update \
    && apt-get -y -qq install python ${BuildDeps}

# installing pip and required python libs
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py
RUN python get-pip.py \
    && pip install --upgrade tqdm

# building coap libs
RUN git clone --depth 1 --recursive -b dtls https://github.com/home-assistant/libcoap.git \
    && cd libcoap \
    && ./autogen.sh \
    && ./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr" \
    && make \
    && make install

# getting tradfri python scripts
RUN git clone https://github.com/hvanderlaan/ikea-smartlight.git
COPY tradfri.cfg /ikea-smartlight/tradfri.cfg

# cleaning up build tools
RUN apt-get -y -qq purge ${BuildDeps} \
    && apt-get -y -qq autoremove \
    && apt-get -y -qq autoclean

WORKDIR /ikea-smartlight/
