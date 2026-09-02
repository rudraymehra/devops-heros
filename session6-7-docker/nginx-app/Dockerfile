# Nginx Hello World
FROM nginx:alpine

# Replace the default welcome page with our own
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
# The base image already defines CMD ["nginx", "-g", "daemon off;"]
