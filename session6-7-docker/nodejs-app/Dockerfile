# Node.js Hello World - Express server
FROM node:18-alpine

# All following commands run relative to /app inside the image
WORKDIR /app

# Copy dependency manifest first so the npm install layer is cached
# as long as package.json does not change
COPY package*.json ./
RUN npm install --omit=dev

# Copy the application source
COPY server.js .

# Documented port the app listens on (does not publish it by itself)
EXPOSE 3000

CMD ["node", "server.js"]
