from alpine:latest

maintainer Harald van der Laan <harald@familievdlaan.nl>

run apk update
run apk add privoxy

run echo "listen-address 0.0.0.0:8118" > /etc/privoxy/config
run echo "forward-socks5t / tor:9050 ." >> /etc/privoxy/config

expose 8118

entrypoint ["privoxy", "--no-daemon"]
cmd ["/etc/privoxy/config"]
