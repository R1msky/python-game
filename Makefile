all: lint exec

lint:
	python3 -m isort -y
	python3 -m flake8 .

exec:
	python3 start.py

install:
	pip3 install --upgrade setuptools pip
	pip3 install -r requirements.txt
