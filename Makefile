VERSION=$(shell python version.py)
SRCDIRS=spec src

all: clean install spec format type

install:
	pip install -r requirements.txt
	pip install -e .

update:
	pip list --outdated --format=freeze | \
		grep -v '^\-e' | cut -d = -f 1  | \
		xargs -n1 pip install --upgrade
	pip freeze --exclude-editable > requirements.txt

spec:
	python -m spec

.PHONY: spec

format:
	black --include '\.pyi?$$' $(SRCDIRS)
	autoflake -ri $(SRCDIRS)
	isort -rc $(SRCDIRS)
	npx prettier --end-of-line lf --write '**/*.{css,html,js,json,md,yaml,yml}'
	sed -i "s/version-[0-9]\+.[0-9]\+.[0-9]\+/version-$(VERSION)/g" README.md
	sed -i "s/ingraph.aws\/[0-9]\+.[0-9]\+.[0-9]\+/ingraph.aws\/$(VERSION)/g" README.md
	sed -i "s/cloudformation-[0-9]\+.[0-9]\+.[0-9]\+/cloudformation-$(shell cat spec/VERSION)/g" README.md

type:
	MYPYPATH=./src mypy --namespace-packages -p ingraph

clean:
	rm -rf .coverage* .mypy_cache .pytest_cache coverage.xml build dist
	find . -name __pycache__ -o -name '*.egg-info' | xargs rm -rf

dist:
	python3 setup.py sdist bdist_wheel

.PHONY: dist
