# Nginx base
FROM nginx:1.19-alpine

# Replacing default gninx configuration
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d