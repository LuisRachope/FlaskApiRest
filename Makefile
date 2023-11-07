install:
	git config --local core.hooksPath .githooks/
	chmod -R +x .githooks
	pip install -r requirements.txt

lint:
	black -l 120 src
	isort -l 120 --profile black src
