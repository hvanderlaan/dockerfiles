# rdesktop

## macOS
### requirements
```bash
brew install xquartz socat
```
### usage
```bash
docker build --force-rm -t <path to dockerfile>
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
DISPLAY="$(ipconfig getifaddr en0):0"
docker run --rm -ti -e DISPLAY=${DISPLAY} --net=host <local docker image> <ipaddress>[:<port>]
```
