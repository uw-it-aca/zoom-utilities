ARG DJANGO_CONTAINER_VERSION=1.4.1

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-container:${DJANGO_CONTAINER_VERSION} as app-prebundler-container

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

#ADD --chown=acait:acait docker/app_start.sh /scripts
#RUN chmod u+x /scripts/app_start.sh

RUN /app/bin/pip install -r requirements.txt

FROM node:lts-bullseye AS node-bundler

ADD ./package.json /app/
WORKDIR /app/
RUN npm install .

ADD . /app/

ARG VUE_DEVTOOLS
ENV VUE_DEVTOOLS=$VUE_DEVTOOLS
RUN npm run build

FROM app-prebundler-container as app-container

COPY --chown=acait:acait --from=node-bundler /app/app_name/static /app/app_name/static

RUN /app/bin/python manage.py collectstatic --noinput

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-container:${DJANGO_CONTAINER_VERSION} as app-test-container

ENV NODE_PATH=/app/lib/node_modules
COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
