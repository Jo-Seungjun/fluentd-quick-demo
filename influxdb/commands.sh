if [ $1 = "influxdb" ]; then
    echo "indluxdb"
    sudo docker run \
        -it \
        --rm \
        --network tempnetwork \
        --name influxdb \
        -p 8086:8086 \
        -p 8086:8086/udp \
        --volume $(pwd)/influxdb2:/var/lib/influxdb2 \
        --volume $(pwd)/config.yml:/etc/influxdb2/config.yml \
        influxdb:2.1.1
fi

if [ $1 = "influx_client" ]; then
    echo "influx_client"
    sudo ./influx config create --config-name default \
        --host-url http://localhost:8086 \
        --org temporg \
        --token j-ctE6B5ikx1oAsAFgXSVvb8VmfgXXmii7cdm0R-zhQyKSNGlaHecSIOqQs25BKylVyU-TwqWrS4ebQMvYW5XA==
        --active
fi