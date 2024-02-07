Testing out a locally running prefect server. 

### Start Server (in one terminal window)
```
$ prefect server start

...


 ___ ___ ___ ___ ___ ___ _____
| _ \ _ \ __| __| __/ __|_   _|
|  _/   / _|| _|| _| (__  | |
|_| |_|_\___|_| |___\___| |_|

Configure Prefect to communicate with the server with:

    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

View the API reference documentation at http://127.0.0.1:4200/docs

Check out the dashboard at http://127.0.0.1:4200
```
And then go to that URL: http://127.0.0.1:4200

### Run Test Pipeline
```
$ poetry install
$ poetry run python nick-prefect/test_prefect.py
```

Run with an argument
```
$ poetry run python nick-prefect/test_prefect.py --name "nick-roberson/places"

13:23:57.991 | INFO    | prefect.engine - Created flow run 'thundering-flounder' for flow 'get-repo-info'
13:23:58.023 | INFO    | Flow run 'thundering-flounder' - Created task run 'get_url-0' for task 'get_url'
13:23:58.024 | INFO    | Flow run 'thundering-flounder' - Executing 'get_url-0' immediately...
13:23:58.447 | INFO    | Task run 'get_url-0' - Finished in state Completed()
13:23:58.447 | WARNING | Task run 'get_url-0' - Task run 'get_url-0' finished in state Completed()
13:23:58.448 | INFO    | Flow run 'thundering-flounder' - PrefectHQ/prefect repository statistics 🤓:
13:23:58.449 | INFO    | Flow run 'thundering-flounder' - Stars 🌠 : 1
13:23:58.449 | INFO    | Flow run 'thundering-flounder' - Forks 🍴 : 0
13:23:58.464 | INFO    | Flow run 'thundering-flounder' - Finished in state Completed()
Result: True
```