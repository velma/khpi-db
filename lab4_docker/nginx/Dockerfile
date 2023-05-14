FROM nginx

COPY index.html /usr/share/nginx/html
ADD custom.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
