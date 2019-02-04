#!/bin/bash
git pull
rm -rf ./_site
JEKYLL_ENV=production jekyll build
sudo rm -rf /var/www/teambrookvale.com.au/html/*
sudo cp -r ./_site/. /var/www/teambrookvale.com.au/html/
sudo chown -R www-data:www-data /var/www/teambrookvale.com.au/
