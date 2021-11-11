docker stop cocutils
docker rm cocutils

docker run -d --name cocutils -v $PWD/output:/src/cocutils/output -v $PWD/coccsv:/src/cocutils/coccsv -v $PWD/cocsc:/src/cocutils/cocsc cocutils