FROM node:16.17.1

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . . 

EXPOSE 10000

CMD ["npm", "start"]