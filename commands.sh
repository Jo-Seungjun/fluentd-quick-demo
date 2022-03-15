
if [ $1 == "build" ]; then
    echo "build"
    sudo docker build -t fluentd .
fi