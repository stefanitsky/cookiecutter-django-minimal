ARG PYTHON_VERSION=3.7

# Build dependencies in separate container
FROM tiangolo/uvicorn-gunicorn:python${PYTHON_VERSION} AS builder
ENV WORKDIR /app
ARG REQUIREMENTS=production
ENV APP_MODULE "config.asgi:application"
# Allows docker to cache installed dependencies between builds
COPY ./requirements ${WORKDIR}/requirements/
RUN cd ${WORKDIR} && pip install -r ./requirements/${REQUIREMENTS}.txt

# Create the final container with the app
FROM tiangolo/uvicorn-gunicorn:python${PYTHON_VERSION}


ENV USER=docker \
    GROUP=docker \
    UID=12345 \
    GID=23456 \
    HOME=/app \
    PYTHONUNBUFFERED=1
WORKDIR ${HOME}

# Create user/group
RUN addgroup --gid "${GID}" "${GROUP}" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "${GROUP}" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"

# Run as docker user
USER ${USER}
# Copy installed packages
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
# Copy the application
COPY --chown=docker:docker . .
