# you have 10 docker containers running on a linux server. you need to write a
# python script to check whether a particular docker container named demo-app 
# is running or stopped. 

import docker

# Connect to Docker daemon
client = docker.from_env()

try:
    # Retrieve php-app container
    container = client.containers.get("php-app")

    # Check container status
    if container.status == "running":
        print("php-app container is running")
    else:
        print("php-app container is stopped")

except docker.errors.NotFound:
    print("php-app container does not exist")

except docker.errors.DockerException as e:
    print("Docker error:", e)
