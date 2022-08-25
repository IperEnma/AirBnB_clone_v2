#!/usr/bin/env bash
#sets up your web servers

package=$(dpkg -s nginx 2> /dev/null | grep nginx | head -1 | cut -d " " -f2 2> /dev/null)
if [ "$package" = "nginx" ]
then
        :
else
        sudo apt update -y
        sudo apt install -y nginx
fi
sudo /etc/init.d/nginx stop
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
file="/data/web_static/releases/test/index.html"
if [[ -e $file ]]
then
        :
else
        sudo touch $file
        sudo echo "Hello World" | sudo tee $file
fi
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo /etc/init.d/nginx start
