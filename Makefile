SHELL := /bin/bash

activate:
	@echo "source .env/bin/activate"

pre-install: #rust for mac
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
	source "$HOME/.cargo/env"

setup:
	pip install transformers
	pip install  sentencepiece
	pip install 'transformers[torch]'
	pip install 'transformers[flax]'
	pip install 'transformers[tf-cpu]'
	
	@echo "Installed! ✅"

run:
	@python script.py

sample:
	python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"


.PHONY: activate