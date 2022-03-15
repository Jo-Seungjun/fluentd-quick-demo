
if [ $1 == "build" ]; then
    echo "Building..."
    sudo docker build -t log_generator .
    echo "Done."
elif [ $1 == "run" ]; then
    echo "Running..."
    sudo docker run \
    -it \
    --rm \
    --name log_generator \
    log_generator
    echo "Done."
elif [ $1 == "log" ]; then
    echo "Docker Log..."
    sudo docker log
    echo "Done."
else
    echo "Usage: ./commands.sh build|run|clean"
fi