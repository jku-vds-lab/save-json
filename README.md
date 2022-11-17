# save-json
Dump python server that stores data as JSON files in the `data/` folder.

### Usage:

* Check if server is running: http://localhost:9666/
* See and test the API via: http://localhost:9666/docs
* Send POST requests to http://localhost:9666/save  
  (e.g., with [Thunder](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client))
  Example JSON: 
  ```json
  {
    "filename": "foobar.json",
    "data": {
      //anything you want to store, e.g.:
      "timestamp": "2022-11-11 11:11",
      "event": "Carnival season kicks off"
    }
  }

## Local Setup
### Docker (no relaod on changes)

```sh
docker-compose up
```

### Python (reloads on code changes)

Create conda environment:
```sh
conda create --name save-json python=3.10
conda activate save-json
conda install --yes --file requirements.txt
```

Start:
```sh
uvicorn save-json.server:app --reload --port 9666
```