(building)

# Basic Docker network for developers

>This is a explanation with examples about `docker network` for developers. Hope you enjoy (:

When we talk about diferent docker services connecting each other, it is implicit that we're using networks. Depending on what you're creating, maybe there is no reasons to worry about create and managing networks because sometimes Docker runs everything for us in background and everything works fine. 

But sometimes we also need to create something different or outside of the box and you're going need to understand what is going on inside your Docker container/services.

## What you're going to find (and not to find) in this tutorial

- [x] A basic `Python + Flask` app that connects in a `MongoDB` database
- [x] `docker run` command line to create and connect containers
- [x] How to create and check basic networks in docker
- [x] Use `Docker Compose` and understant what is going on under the covers
- [x] Understand how `docker` use `networks` to connect different `containers/services`
- [x] How can you find what is wrong with your services connection issues
- [ ] Learn how to use advanced `docker networks`
- [ ] Learn how to configure `Docker Compose`
- [ ] Get it all the basics for running containers and services on docker 

## What is a network in Docker?

First things first, Docker use networks for what? Well, the answer is simple: for the same reason that any PC or virtual machine also use them to share and consume third parties resources. 

Every computer machine that need to connect with some outside world feature will need a network interface for doing that. The same will happen with Docker. When we start a container, Docker will automatically connect him on the netowrk system. 

It'll be nice see that in action, right? 

So let's get started.

---

## 1. Image creation
>In this example we're going to create an image with a Python Flask application that return "It works" on accessing localhost/test and connects in a database and return data in localhost/. To use this, first we need to create the image. If you already know how to build and start a container, go to the xx step.

<details>

In the /tutorial folder, type the command below:

`docker build . -t tutorial-image`

This going to create an image for the Dockerfile in that folder. This file includes just two important elements:

1. the installation of all dependencies inside the requirements.txt file that includes `Flask` and `flask-mongoengine` packages
2. the exposure of the 5000 port that is default by using Flask

After run the command, we can check if the image was created by typing `docker images`:

![image](/assets/img/0.png)

</details>

---
## 2. Running the image
> After build the image, next step consist in running the container and testing him.
<details>

To running the image, we can type the command below:

`docker run --name tutorial-container -p 80:5000 -d tutorial-image`

After running the command above, we can check this out by typing the `docker ps` and searching for the "tutorial-container" in the list.

<div>

![image](/assets/img/0.1.png)
</div>

If the status is up and running, this means that we're able to access the `flask` application on the following address: `http://localhost/test` and see the API "It works!" result.

<div align="center">

![image](/assets/img/1.png)

</div>

Here is what the command are actually doing:

1. --name able us to set a name to the container, as can be verified in the `docker ps` result. If we skip this, Docker will set a name randomly for us.
2. -p flag is very important to make the application works. If we jump over this, nothing will work by accessing localhost/test. -p means that we're connecting the 80 port of the host to the 5000 port of the container. Remember the `expose 5000` in the Dockerfile and that the Flask uses this port by default? Whitout this flag we're not able to reach the application running inside the container.
3. -d flag is just to run the container in background mode, so we can keep using the terminal to run some other commands.
4. Last but not least, the "tutorial-image" is just the image that we wanna run.

</details>


## Where is the network?
> After running a container, where is the network default functionality applyed by Docker?

<details>

By default, Docker have three default network modes: bridge, host and none. We can see this by typing `docker network ls`:

![image](/assets/img/2.png)

Those are some of the [default Docker network drivers](https://docs.docker.com/network/). Bridge, the first one, as his name suggests, is used by containers that need to communicate. This is the default network driver of any container when we don't specify a driver. Also, this is the most commom drive that we're going to use for simple services aplications.

Host is a driver that allows the container bind to the host network. If we used this driver, that means the container would beacome just like any other machine insede the network host.

Finally, the none driver means that really there is none network enable on the running container.

In the [Docker documentation there is also the overlay, ipvlan and macvlan](https://docs.docker.com/network/) drivers. But in this article we're going to use bridge only. If you want more examples of those other drivers, check out the [conclusion](#conclusion) topic after reading (:


</details>



<!--Docker implements the "networks" top level definition for network config for services. Using that resource, we can provide a default configuration on running containers and other composes.

Docker by default creates tree network: bridge, host and none.

-------docker network ls image

## bridge

Create a bridge between containers. Can be used to connect services. When a docker-compose with multiple services up, docker create a default network for connection between services layers.

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

# Conclusion

We saw some basics from Docker Network. Now, if you want to get some more complex or other network definitions, you can take <a src="https://www.youtube.com/watch?v=bKFMS5C4CG0">this tutorial</a> from NetworkChuck. I not gonna lie. Crazy amazing complex shit on that video. Get a look if you want to dive into network or in devops career. -->