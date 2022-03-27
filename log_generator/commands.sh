FLUENTD_HOST="localhost:24224"
IMAGE_NAME="log_generator"
NAME="log_generator"

if [ $1 = "build" ]; then
    echo "Building..."
    sudo docker build -t ${IMAGE_NAME} .
fi

if [ $1 = "run" ]; then
    echo "Running..."
    sudo docker run \
        -it \
        --rm \
        --log-driver=fluentd \
        --log-opt fluentd-address=${FLUENTD_HOST} \
        --log-opt tag="docker.log.{{.Name}}" \
        --name ${NAME} \
        ${IMAGE_NAME}
fi

if [ $1 = "log" ]; then
    echo "Docker Log..."
    sudo docker log ${NAME}
fi