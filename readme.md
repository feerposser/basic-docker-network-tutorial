(building)

# Basic Docker network for developers

>This is a explanation with examples about `docker network` for developers. Hope you enjoy (:

When we talk about diferent docker services connecting each other, it is implicit that we're using networks. Depending on what you're creating, maybe there is no reasons to worry about create and managing networks because sometimes Docker runs everything for us in background and everything works fine. 

But sometimes we also need to create something different or outside of the box and you're going need to understand what is going on inside your Docker container/services.

## What you're going to find (and not to find) in this tutorial

- [x] A basic `Python + Flask` app that connects in a `MongoDB` database
- [x] `Docker run` command line to create and connect containers
- [x] How to create and check basic networks in docker
- [x] Use `Docker Compose` and understant what is going on under the covers
- [x] Understand how `docker` uses `networks` to connect `containers/services`
- [x] How can you find what is wrong with your services connection issues
- [ ] Learn how to use advanced `docker networks`
- [ ] Learn how to configure `Docker Compose`
- [ ] Get all the basics for running containers and services on docker 






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






# Conclusion

We saw some basics from Docker Network. Now, if you want to get some more complex or other network definitions, you can take <a src="https://www.youtube.com/watch?v=bKFMS5C4CG0">this tutorial</a> from NetworkChuck. I not gonna lie. Crazy amazing complex shit on that video. Get a look if you want to dive into network or in devops career.