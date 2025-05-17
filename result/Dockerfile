FROM node:18-slim

# Install curl and ensure Yarn is available
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/* && \
    corepack enable

WORKDIR /usr/local/app

# Copy Yarn files
COPY package.json yarn.lock ./

# Install dependencies with Yarn
RUN yarn install

# Copy application code
COPY . .

EXPOSE 8081
CMD ["node", "server.js"]