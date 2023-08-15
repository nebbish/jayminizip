rm -rf ./dist ./jayminizip.egg-info && python3 setup.py sdist && twine upload dist/*
