# Apache HTTP Server Hello World
FROM httpd:2.4-alpine

# Replace the default "It works!" page with our own
COPY index.html /usr/local/apache2/htdocs/index.html

EXPOSE 80
# The base image already defines CMD ["httpd-foreground"], so no CMD needed here
