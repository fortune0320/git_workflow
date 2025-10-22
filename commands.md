# Build the docker image

docker build -t docker-volume-exercize .

# Run the docker container

docker run -v local/pc/directory/here:/app/data docker-volume-exercize
