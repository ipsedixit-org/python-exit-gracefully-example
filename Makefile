REQUIREMENTS_IN_FILES = requirements.in requirements_test.in

setup:
	python3 -m venv .venv ; \
	. .venv/bin/activate ; \
	pip install -r requirements.txt ;\
	pip install -r requirements_test.txt

update-reqs:
	@echo "$@"
	virtualenv -p python3.10 /tmp/venv ; \
    . /tmp/venv/bin/activate ; \
    pip install pip-tools==6.8.0 ; \
    for REQUIREMENT_FILE in $(REQUIREMENTS_IN_FILES) ; do \
        BASE_OUTPUT_FILE=`echo $${REQUIREMENT_FILE} | sed s/.in//` ; \
        OUTPUT_FILE="$${BASE_OUTPUT_FILE}.txt" ; \
        # Install previous requirements in order to avoid errors \
        pip install -r "$${OUTPUT_FILE}" ; \
        pip install -r "$${REQUIREMENT_FILE}" ; \
        echo "REQUIREMENT_FILE: $${REQUIREMENT_FILE} --> OUTPUT_FILE: $${OUTPUT_FILE}" ; \
        pip-compile --no-emit-trusted-host --no-emit-index-url --build-isolation -o $${OUTPUT_FILE} $${REQUIREMENT_FILE} -v ; \
        RESULT=$$? ; \
        if [ $${RESULT} -ne 0 ]; then \
            echo "An error occurred in pip-compile for REQUIREMENT_FILE: $${REQUIREMENT_FILE} --> OUTPUT_FILE: $${OUTPUT_FILE}" ; \
            exit 2 ; \
        fi ; \
    done ; \
    rm -fR /tmp/venv

test:
	pytest --log-cli-level DEBUG --capture=tee-sys --cov=python_exit_gracefully_example tests

lint:
	black python_exit_gracefully_example tests
	isort python_exit_gracefully_example tests

pep8:
	flake8 python_exit_gracefully_example tests

tox:
	tox -e tests,pep8
