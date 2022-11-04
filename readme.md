(building)

# Basic Docker network for developers part 1

>This is a explanation with examples of `docker network` for developers. Hope you enjoy (:

When we talk about different docker services connecting each other, it is implicit that we're using networks. Depending on what you're creating, maybe there are no reasons to worry about creating and managing networks because sometimes Docker runs everything for us in the background and everything works fine. 

But sometimes we also need to create something different or outside of the box and you're going to need to understand what is going on inside your Docker container/services.

## What you're going to find (and not to find) in this tutorial

- [x] A basic `Python + Flask` app that connects to a `MongoDB` database
- [x] `docker run` command line to create and connect containers
- [x] How to create and check basic networks in docker
- [x] Understand how `docker` uses `networks` to connect different `containers/services`
- [x] How can you find what is wrong with your services connection issues
- [ ] Use `Docker Compose` and understand what is going on under the covers
- [ ] Learn how to use advanced `docker networks`
- [ ] Learn how to configure `Docker Compose`
- [ ] Get it all the basics for running containers and services on docker 

## What is a network in Docker?

First things first, Docker use networks for what? Well, the answer is simple: for the same reason that any PC or virtual machine also use them to share and consume third parties resources. 

Every computer machine that needs to connect with some outside world feature will need a network interface for doing that. The same will happen with Docker. When we start a container, Docker will automatically connect it on the netowrk system. 

It'll be nice see that in action, right? 

So let's get started.

---

## 1. Image creation
>In this example we're going to create an image with a Python Flask application that returns "It works" on accessing localhost/test and connects in a database and return data in localhost/. To use this, first we need to create the image. If you already know how to build and start a container, go to the [3 step](#3-where-is-the-network).

<details>

In the /tutorial folder, type the command below:

`docker build . -t tutorial-image`

This going to create an image using the Dockerfile in that folder. This file includes just two important elements:

1. the installation of all dependencies inside the requirements.txt file that includes `Flask` and `flask-mongoengine` packages
2. the exposure of the 5000 port that is default when using Flask

After running the command, we can check if the image was created by typing `docker images`:

![image](/assets/img/0.png)

</details>

---
## 2. Running the image
> After build the image, next step consist in running the container and testing him.
<details>

To run the image, we can type the command below:

`docker run --name tutorial-container -p 80:5000 -d tutorial-image`

After running the command above, we can check this out by typing the `docker ps` and searching for the "tutorial-container" in the list.

<div>

![image](/assets/img/0.1.png)
</div>

If the status is up and running, this means that we're able to access the `flask` application on the following address: `http://localhost/test` and see the API result telling that "It works!".

<div align="center">

![image](/assets/img/1.png)

</div>

Here is what the command is actually doing:

1. --name able us to set a name to the container, as can be verified in the `docker ps` result. If we skip this, Docker will set a name randomly for us.
2. -p flag is very important to make the application works. If we jump over this, nothing will work by accessing localhost/test. -p means that we're connecting the 80 port of the host to the 5000 port of the container. Remember the `expose 5000` in the Dockerfile and that the Flask uses this port by default? Whitout this flag we're not able to reach the application running inside the container.
3. -d flag is just to run the container in background mode, so we can keep using the terminal to run some other commands.
4. Last but not least, the "tutorial-image" is just the image that we wanna run.

</details>


## 3 Where is the network?
> After running a container, where is the network default functionality applyed by Docker?

<details>

By default, Docker have three default network modes: bridge, host and none. We can see this by typing `docker network ls`:

![image](/assets/img/2.png)

Those are some of the [default Docker network drivers](https://docs.docker.com/network/). Bridge, the first one, as his name suggests, is used by containers that need to communicate. This is the default network driver of any container when we don't specify a driver. Also, this is the most commom drive that we're going to use for simple services aplications and architectures.

Host is a driver that allows the container bind to the host network. If we used this driver, that means the container would beacome just like any other machine inside the network host.

Finally, the none driver means that really there is none network enable on the running container.

><small>In the [Docker documentation there are also the overlay, ipvlan and macvlan](https://docs.docker.com/network/) drivers. But in this article we're going to use bridge only. If you want more examples of those other drivers, check out the [conclusion](#4-conclusion) topic after reading (:</small>

As we saw, bridge is the default driver of any non specified network container. So, our tutorial-container must be using this driver. We can see whether this is true by accessing the network or the container inspector.

Typing `docker network inspect bridge` it will show us the bridge driver configuration. And in some point there is an object called "Containers" that contains all the containers using this driver.

<div align="center">

![image](/assets/img/3.png)

</div>

And the `docker container inspect tutorial-container` also will show us the inspector where in some point it'll be and object called "Networks" that list the networks used by the tutorial-container.

<div align="center">

![image](/assets/img/4.png)

</div>

</details>

Now we know that all the containers use this driver by default. That means we can connect them through this network, right? 

So in the next step we going to create a database container which 'tutorial-container' can access.

---

## 3.1 Connecting containers in a network
> In this step we're going to create a database container which can be accessed by the 'tutorial-container'.

<details>
First things first, let's access the `localhost/` address and see what happens.

<div align="center">

![image](/assets/img/5.png)
<small>If you try it, you'll get an 500 error.</small>
</div>

This is happening because when we try to reach the localhost root address, the `Flask` application try to connect in a `Mongodb` database and retrieve all the data inside it. You can verify this by openning and reading the comments whithin the [app.py file in the tutorial folder](/tutorial/app.py).

> To solve this problem, let's try to create a Mongo container.

First things first, let's take a look on the [MongoDB Docker image documentation](https://hub.docker.com/_/mongo). To create a container using Mongo we can run the "mongo" official image and set the environment variables to match with the ones in the app.py file. If you don't know what are the environment variables, take a look on my previus post by [clicking here](https://feerposser.medium.com/docker-and-docker-compose-env-file-tutorial-daefb5605e0e).

`docker run -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin -d --name tutorial-mongo-container mongo`

If you don't have the mongo image on your local cache, Docker will download it on Docker Hub and run the container with name "tutorial-mongo-container" or any other name that you want.  You can check this out by typing `docker images` and `docker ps` to check the mongo image followed by the running container.

And as you can imagine, while the container has been created, Docker set him to the bridge network driver.

We can run the same command used before to get a list of containers using bridge driver: `docker network inspect bridge`. And in the containers list we can found the mongodb container.

<div align="center">

![](/assets/img/6.png)
<small>The same will happen if we run "docker container inspect tutorial-mongo-container". Bridge will be there in the network settings.</small>
</div>

Now, when we access the `localhost`, maybe a empty list of data will be sort in the screem, right?

The answer is: no. The same Internal Server Error will appear. 

This is happening because we need to connect both containers in a same network.

</details>

## 3.2 Creating a network
> In this section we'll create a bridge network and connect both containers on it. 

<details>

To do this, first let's stop the containers and after the network creation we can start them using the container network flag.

`docker stop tutorial-mongo-container tutorial-container`

To create a new Docker bridge network, just type the command below:

`docker network create tutorial-network`

Docker uses the bridge driver as default to create containers and also to create networks. Running `docker network ls` you be able to see the network in the list:

<div align="center">

![image](/assets/img/7.png)

</div>

Now, when we run the containers we must use the --network flag to specify the network that we just created. 

`docker run -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin -d --name tutorial-mongo-container --network tutorial-network mongo`

`docker run --name tutorial-container -p 80:5000 -d --network tutorial-network tutorial-image`

To certify that both containers are in the same network, we can inspect the tutrial-network by typing

`docker network inspect tutorial-network`

<div align="center">

![image](/assets/img/8.png)

</div>

And when we access the `localhost`, we expect to see a empty list of data. But this will not happn. The same Internal Server Error will appear. But Why?

The answer is simple. In the app.py file, on the mongodb configuration, the "host" attribute need to be set with the database ip address or domain. 

But when we're using Docker in this situation, we do not need to get the ip address and set it manually. We can just use the container name as the domain because Docker implements an internal DNS (Domain Name Service) that can handdle everything for us. Cool isn't it?

The tutorial-image generated with the app.py are using "mongo" as the domain name of the database. To be able to connect in our mongo container we can fix in two ways:

1. Stop the tutorial-container, delete its image, update the app.py file to use the name of our container, build the image again and run the container.
2. Just stop the mongo container and start it again using "mongo" as the container name.

As the second solution is  simpler for this example, I'll choose this one. 

1. docker stop tutorial-mongo-container
2. docker run -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin -d --network tutorial-network --name mongo mongo

<div align="center">

![](/assets/img/9.png)

</div>

Now our application container is successfully reaching the database container and retrieve all its data (in this case there is no one, but you get the idea).

</details>

# 4 Conclusion

We saw some basics from Docker Network. Now, if you want to get some more complex or other network definitions, you can take a look in <a src="https://www.youtube.com/watch?v=bKFMS5C4CG0">this tutorial</a> from NetworkChuck. I not gonna lie. Crazy amazing complex stuff on that video. Most part of the time you don't need to configure all those things if you're a developer and not a professional devops. 

And if you want to read a little more about Docker networks, get a look in [this post of Docker's blog](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/) to understand more from what happn behind the scenes.

Cheers (: