FROM node:22-alpine AS builder
LABEL stage="builder"

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build


FROM caddy:2.8-alpine AS runner

WORKDIR /app

COPY Caddyfile.prod ./Caddyfile
COPY --from=builder /app/dist .

EXPOSE 8001

ENTRYPOINT [ "caddy", "run" ]
