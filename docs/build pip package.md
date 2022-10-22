# build pip package

## create env
```
conda create -n py36 python=3.6 -y
conda activate py36
```

## fetch code
```
git clone https://github.com/StudyExchange/LessLine.git
cd LessLine
```

## tests
```
pip install -r requirements-tests.txt
pytest -s ./tests
```

## package
```
python setup.py build
python setup.py sdist
python setup.py bdist_wheel
# pip uninstall lessline
pip install .\dist\lessline-0.1.0-py3-none-any.whl --force-reinstall
```

## release
```
pip install twine
twine upload ./dist/*
```
