
if [ $1 = "fluentd-build" ]; then
    echo "build"
    sudo docker build -t fluentd_custom .
fi

if [ $1 = "fluentd" ]; then
    echo "fluentd"
    sudo docker run \
        -it \
        --rm \
        --network tempnetwork \
        --name fluentd \
        -p 24224:24224 \
        -p 24224:24224/udp \
        fluentd_custom
fi

