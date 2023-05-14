FROM postgres:15.2

RUN apt update -y  \
    && apt upgrade -y \
    && apt install -y postgresql-15-pgmemcache \
    && rm -rf /var/lib/apt/lists/*
