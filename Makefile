NB_FILES = $(shell find . -not -path "*/.ipynb_checkpoints/*" -name "*.ipynb")

clean_nb_output: $(NB_FILES)
	jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace  $^

