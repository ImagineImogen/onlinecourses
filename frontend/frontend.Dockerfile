FROM node:10

WORKDIR /app

RUN mkdir -p /code/frontend

COPY package.json ./

COPY package-lock.json ./

RUN npm install

COPY . .

CMD [ "npm", "start" ]