install:
	git config --local core.hooksPath .githooks/
	chmod -R +x .githooks
	pip install -r requirements.txt
