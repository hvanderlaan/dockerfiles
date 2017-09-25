# tradfri docker
docker version of the tradfri scripts, this will build all requirements for using tradfri

# usage
```bash
docker build --force-rm -t tradfri .
docker run --rm -ti --net=host tradfri ./tradfri-status.py
docker run --rm -ti --net=host tradfri ./tradfri-lights.py --help
docker run --rm -ti --net=host tradfri ./tradfri-groups.py --help
```

# NOTE
the docker requires a configuration file ```tradfri.cfg``` please change the values to the correct values of the tradfri hub.
