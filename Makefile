.PHONY: tests

PYTHON_ENV = .venv/bin/python

install:
	uv pip install -e '.[dev,s3,azure,hf]'

install-dev:
	uv pip install -e '.[dev]'

install-uv:
	brew install uv

setup-enterprise-modscan:
	helm install -f integration-tests/enterprise-modscan/config.yaml hl-installer oci://quay.io/hiddenlayer/distro-enterprise-platform-installer \
	--set installer.authentication.hl_username=${QUAY_USERNAME} \
	--set installer.authentication.hl_password=${QUAY_PASSWORD} \
	--set modelscanner-v3.orchestrator.license=${HL_LICENSE} \
	--wait --wait-for-jobs && \
	kubectl -n hl-aisec-platform logs -f job/hl-aisec-platform --pod-running-timeout=20s && \
	kubectl port-forward svc/modelscanner-orchestrator 8000 -n hl-modelscanner &>/dev/null &

teardown-enterprise-modscan:
	helm uninstall modelscanner-orchestrator --namespace=hl-modelscanner && \
	helm uninstall modelscanner-redis --namespace=hl-modelscanner && \
	helm uninstall modelscanner-minio --namespace=hl-modelscanner && \
	helm uninstall hl-installer

tests:
	pytest -sv tests/

venv:
	uv venv

lint:
	$(PYTHON_ENV) -m ruff check .

format:
	$(PYTHON_ENV) -m ruff format .
