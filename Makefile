TARGETS := agraffe

format:
	isort ${TARGETS}
	black ${TARGETS}

lint:
	isort --check-only ${TARGETS}
	black --check ${TARGETS}
	flake8 --config format.ini ${TARGETS}
	mypy --config-file format.ini ${TARGETS}
