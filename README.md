Testing out a locally running prefect server. 

How to start server (in one terminal window)
```
$ prefect server start
```

How to run test pipeline (in another terminal window)
```
$ poetry install
$ poetry run python nick-prefect/test_prefect.py
```