.PHONY: tests

PYTHON_ENV = .venv/bin/python

install:
	uv pip install -e '.[dev,s3,azure,hf]'

install-dev:
	uv pip install -e '.[dev]'

install-uv:
	brew install uv

create-kind-cluster:
	kind create cluster --config integration-tests/enterprise-modscan/kind.yaml

setup-enterprise-modscan:
	helm install -f integration-tests/enterprise-modscan/config.yaml hl-installer oci://quay.io/hiddenlayer/distro-enterprise-platform-installer \
	--set installer.authentication.username=${QUAY_USERNAME} \
	--set installer.authentication.password=${QUAY_PASSWORD} \
	--set modelscanner.orchestrator.license=${HL_LICENSE} \
	--wait --wait-for-jobs && \
	kubectl -n hl-aisec-platform logs -f job/hl-aisec-platform-1 --pod-running-timeout=20s

port-forward-service:
	kubectl port-forward svc/modelscanner-minio 9000:9000 -n hl-modelscanner &>/dev/null & \
	kubectl port-forward svc/modelscanner-orchestrator 8000 -n hl-modelscanner &>/dev/null &

add-minio-bucket:
	$(eval MINIO_ROOT_USER := $(shell kubectl get secret -n hl-modelscanner modelscanner-minio -o json | jq -r .data.rootUser | base64 --decode))
	$(eval MINIO_ROOT_PASSWORD := $(shell kubectl get secret -n hl-modelscanner modelscanner-minio -o json | jq -r .data.rootPassword | base64 --decode))
	mc alias set myminio http://127.0.0.1:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD} && \
	mc mb myminio/hl-adhoc-model-stage

setup-s3-dns:
	sudo echo "127.0.0.1 modelscanner-minio.hl-modelscanner" | sudo tee -a /etc/hosts

teardown-enterprise-modscan:
	helm uninstall modelscanner-orchestrator --namespace=hl-modelscanner && \
	helm uninstall modelscanner-redis --namespace=hl-modelscanner && \
	helm uninstall modelscanner-minio --namespace=hl-modelscanner && \
	helm uninstall hl-installer

teardown-kind-cluster:
	kind delete cluster --name=test-cluster

tests:
	pytest -sv tests/

venv:
	uv venv

lint:
	$(PYTHON_ENV) -m ruff check .

format:
	$(PYTHON_ENV) -m ruff format .
