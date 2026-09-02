# -------------------------
# Stage 1: Build
# Installs ALL dependencies (including devDependencies) and prepares the app.
# Nothing from this stage ends up in the final image unless we COPY it over.
# -------------------------
FROM node:24-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# -------------------------
# Stage 2: Production
# Starts again from a clean base image and only brings in what is needed
# to run the app: package files, production dependencies and server.js.
# -------------------------
FROM node:24-alpine AS production
ENV NODE_ENV=production \
    PORT=8080
WORKDIR /app

COPY --from=builder /app/package*.json ./
RUN npm install --omit=dev && npm cache clean --force
COPY --from=builder /app/server.js ./

# Run as the unprivileged "node" user that ships with the official image
RUN chown -R node:node /app
USER node

EXPOSE 8080
CMD ["node", "server.js"]
