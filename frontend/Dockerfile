FROM node:21.7.0-alpine3.19
WORKDIR /app

COPY package*.json ./
RUN npm ----legacy-peer-deps install

COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev"]