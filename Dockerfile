FROM node:22-alpine

WORKDIR /app

RUN corepack use pnpm@10.32.1

RUN corepack enable

COPY . .

WORKDIR /app/javascript

RUN pnpm install --no-lockfile --no-cache

CMD ["pnpm", "run", "db:deploy"]