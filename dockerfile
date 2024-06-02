FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
COPY . .
RUN npm install
ENV VITE_HOST=0.0.0.0
ENV VITE_PORT=5173
CMD ["npm", "run", "dev"]

