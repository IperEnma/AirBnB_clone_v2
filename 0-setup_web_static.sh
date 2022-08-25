#!/usr/bin/env bash
#sets up your web servers

sudo apt update -y
sudo apt install -y nginx
sudo /etc/init.d/nginx stop
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/server_name _;/a location /hbnb_static { alias /data/web_static/current;}' /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
