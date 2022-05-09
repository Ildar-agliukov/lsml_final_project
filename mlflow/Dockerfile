FROM python:3.7

ENV MLFLOW_HOME /opt/mlflow
ENV SERVER_PORT 5000
ENV SERVER_HOST 0.0.0.0
ENV FILE_STORE ${MLFLOW_HOME}/fileStore
ENV ARTIFACT_STORE ${MLFLOW_HOME}/artifactStore

RUN pip install mlflow psycopg2 && \
    mkdir -p ${MLFLOW_HOME}/scripts && \
    mkdir -p ${FILE_STORE} && \
    mkdir -p ${ARTIFACT_STORE}

EXPOSE ${SERVER_PORT}/tcp

WORKDIR ${MLFLOW_HOME}
