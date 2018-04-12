FROM node:6-alpine

ADD package.json /app/package.json

RUN cd /app && npm install
COPY . /app/

CMD ["node", "/app/server.js"]