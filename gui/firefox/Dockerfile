FROM alpine:latest
LABEL maintainer "Harald van der Laan"

ENV URL https://www.google.com

RUN apk --no-cache --update add firefox-esr dbus-x11 ttf-ubuntu-font-family glu
RUN adduser -S firefox

USER firefox

CMD firefox --new-instance ${URL}
