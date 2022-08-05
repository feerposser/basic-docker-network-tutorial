# Docker network example and explanation

>This is a explanation with examples about docker network. Hope you enjoy (:

When we talk about diferent docker services connecting one another, it is implicit that we're using networks. Depending on what you're coding, maybe there is no reasons to worry about create and managing networks because many times Docker runs everything for us. 

But sometimes we also need to create something different or outside of the box and you're going to need to understand what is going on inside your Docker container.

------------------------------------------------------

Docker implements the "networks" top level definition for network config for services. Using that resource, we can provide a default configuration on running containers and other composes.

Docker by default creates tree network: bridge, host and none.

-------docker network ls image

## bridge

Create a bridge between containers. Can be used for connect services. When a docker-compose with multiple services up, docker create a default network for connection between services layers.

--------- IMAGE 1

Every service in the compose will be configured with this default network.

```docker
docker container inspect container-name
```

-------- IMAGE 2

Docker uses the default created network for connections between services. This allows a service connect to another using the name of the service as an alias for the host address.
Imagine two services in a compose: curl and app. Curl could connect to app using
```bash
curl http://app
```



### First step

First things first, let's up 
