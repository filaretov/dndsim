NB_FILES = $(shell find . -not -path "*/.ipynb_checkpoints/*" -name "*.ipynb")

test:
	poetry run pytest --cov=dndsim --cov-report=html tests

clean_nb_output: $(NB_FILES)
	jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace  $^
