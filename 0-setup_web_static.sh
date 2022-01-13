#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

apt-get update -y
apt-get install nginx -y
service nginx restart
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu: data
sed -i "/server_name _/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
nginx -s reload
service nginx restart
