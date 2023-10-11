FROM python:3.11-slim
USER root

# Set the working directory in the container
ARG FUNCTION_DIR=/app
WORKDIR ${FUNCTION_DIR}

# Install the required dependencies using caching
COPY requirements.txt ${FUNCTION_DIR}
RUN --mount=type=cache,target=/root/.cache/pip pip install -r  requirements.txt
RUN pip install gunicorn

# Copy the Lambda function code into the container
WORKDIR ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}
COPY api.py ${FUNCTION_DIR}
COPY config.py ${FUNCTION_DIR}
COPY db.py ${FUNCTION_DIR}
COPY run.py ${FUNCTION_DIR}
COPY user.py ${FUNCTION_DIR}
COPY utils.py ${FUNCTION_DIR}
COPY test.py ${FUNCTION_DIR}

#Set a default value, you can override it during the Docker build
EXPOSE 5000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "run:app"]