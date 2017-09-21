## docker-tor
docker containers for running a http tor proxy. this docker contains two containers for getting a tor proxy setup. a tor container that will connect to the tor network and privoxy container for creating a http proxy.

## usage
```bash
cd tor-proxy
docker-compose up -d
curl -x http://localhost:8118 -ksSL https://check.torproject.org/api/ip
```
