# Dockerfiles
Dockerfiles is a set of containerized applications, tools and services. This set will grow over time.

## usage
```bash
# without docker-compose.yml
docker build --force-rm -t <local image name> <path to Dockerfile>
docker run --rm -ri [options] <local image name> [arguments]

# with docker-compose.yml
docker-compose up <path to docker-compose.yml> [-d] [arguments]
docker-compose down -v --rmi all
```

## Todo
[ ] create docker-compose.yml for all dockers
[ ] add more containers
