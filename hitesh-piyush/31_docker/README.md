### Docker commands that I need to know

```
docker images
```
Tells us about the images(Templates available)

```
docker container
```
Tells us about the containers(Active Machines)

```
docker build -t "${IMAGE_NAME}" .
```

Uses `Dockerfile` to produce an image with its specified name in the current directory


```
docker run -ti "my_image"
```
Makes a container with `my_image` and can also accept arguments

```
docker run -ti node:20-alpine sh
```
runs a light-weight alpine image with node20 installed in shell mode(alpine dont have bash)

```
docker run --rm -it ubuntu
```
Run ubuntu in interactive mode, simulate a tty terminal and --rm removes the container as soon as it is exited

```
docker run -P -it ubuntu
```
-P gives automatic port forwarding, which can be seen with `docker ps` what port is forwarded to what port of the host machine

```
docker run -p 3000:8000 -ti ubuntu
```
Port 8000 of container is mapped to 3000 of the host, manual port mapping
