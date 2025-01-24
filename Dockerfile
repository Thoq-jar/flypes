# basic setup
FROM debian:bullseye-slim
WORKDIR /app

# install python and curl
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl

# install nodejs
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# copy files
COPY . .

# setup python virtual environment
RUN python3 -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# install deps and build
RUN npm install
RUN npm run build

# run
EXPOSE 8080
CMD ["npm", "run", "start"]
