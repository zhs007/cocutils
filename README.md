# cocutils

First, you need get the csv project.

```
sh getcoccsv.sh
```

And then, you need copy the *.sc to ./cocsc/

Now, you can run the project.

```
pip install -r requirements.env.txt
pip install -r requirements.txt

python main.py
```

Or, you can use the Docker.

```
sh builddocker.sh
sh rundocker.sh
```