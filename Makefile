
.PHONY: install
install: ## install pibooth on your raspberry pi
	sudo apt-get install libopenjp2-7
	sudo apt-get install libtiff5
	sudo apt-get install libjpeg8-dev
	pip install -r requirements.txt

.PHONY: start
start: ## start pibooth on your raspberry pi
	python start.py