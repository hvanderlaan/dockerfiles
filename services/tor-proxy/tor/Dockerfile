from alpine:latest

maintainer Harald van der Laan <harald@familievdlaan.nl>

run apk update
run apk add tor --update-cache --repository http://nl.alpinelinux.org/alpine/edge/testing

run echo "SOCKSPort 0.0.0.0:9050" > /etc/tor/torrc.default

expose 9050

entrypoint ["tor", "-f"]
cmd ["/etc/tor/torrc.default"]
