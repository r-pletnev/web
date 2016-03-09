rm /etc/nginx/sites-enabled/*.conf
rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo ln -s /home/box/web/etc/guncorn.conf.py  /etc/gunicorn.d/test
gunicorn -c etc/gunicorn.conf.py hello:app
