# p2000
p2000 is a container that allows you to see the dutch emergency services messages. it was containerized because so it can be used on all systems that can run docker.

## usage
### build
```bash
docker build --force-rm -t <local image name> .
```

### run
```bash
docker run -ti --rm <local image name> [-h] [-r <region code>] [-l <amount of lines>]
```
