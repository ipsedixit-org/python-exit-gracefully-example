# Python exit gracefully example




## Initial setup
Create virtualenv with all dependencies using make command:
```bash
make setup
```

## Execute 
```bash
source .venv/bin/activate
python python_exit_gracefully_example/main.py
```

## Update requirements 
```bash
make update-reqs
```

## Code linting
Code linting has been done using (black)[https://github.com/psf/black] and (isort)[https://pycqa.github.io/isort/].
```bash
source .venv/bin/activate
make lint
```

## Execute tox 
```bash
tox -e tests,pep8
```
