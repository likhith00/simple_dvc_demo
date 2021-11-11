create env

```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```
created a requirments file

install the requirments
```bash
pip install -r requirements.txt
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

updates for readme
```bash
git add .

git commit -m "first commit"

git add . && git commit -m "update Readme.md"

git push origin main
```
tox command - 
```bash
tox
```

for rebuilding - 
```bash
tox -r
```

pytest
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package commands -
```bash
python setup.py sdist bdist_wheel
```
create an artifacts folder

mlflow server command - 

mlflow server \
    --backend-store-uri sqlite:///mlflowdb \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234


