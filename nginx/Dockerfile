FROM nginx:1.15-alpine
MAINTAINER Vito Galvez "vitogalv@buffalo.edu"
RUN rm /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/logs
RUN touch /etc/nginx/logs/error.log
RUN touch /etc/nginx/logs/nginx.pid
RUN touch /etc/nginx/logs/access.log
COPY nginx.conf /etc/nginx/nginx.conf
