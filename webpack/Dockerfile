FROM node:8.16
MAINTAINER Vito Galvez vitogalvez29@gmail.com
RUN mkdir /code
WORKDIR /code
COPY package.json /code/
RUN npm install
COPY . /code/
RUN ./node_modules/.bin/webpack --config webpack.config.js
ENTRYPOINT node server.js
