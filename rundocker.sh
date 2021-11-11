docker stop cocutils
docker rm cocutils

docker run -d --name cocutils -v $PWD/output:/src/cocutils/output cocutils