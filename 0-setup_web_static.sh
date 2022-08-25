#!/usr/bin/env bash
#sets up your web servers
package=$(dpkg -s nginx 2> /dev/null | grep nginx | head -1 | cut -d " " -f2 2> /dev/null)
if [ "$package" = "nginx" ]
then
        :
else
        sudo apt update -y
        sudo apt install -y nginx
        sudo chmod -R 777 /var/www/html
        sudo echo "Hello World" | sudo tee /var/www/html/index.html
        sudo /etc/init.d/nginx stop
        sudo sed -i '/server_name _;/a rewrite ^/redirect_me https://https://www.youtube.com/watch?v=QH2-TGUlwu4/$1 permanent;' /etc/nginx/sites-available/default
        sudo echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom.html
        sudo sed -i '/server_name _;/a error_page 404 /custom.html;' /etc/nginx/sites-available/default
        var=$(cat /proc/sys/kernel/hostname)
        sudo sed -i '/http {/a add_header X-Served-By '"${var}"';' /etc/nginx/nginx.conf
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
sudo sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static/ {\n\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo /etc/init.d/nginx start
