#!/bin/bash
# Install Ruby Gems to ~/gems
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
cd /home/ubuntu/teambrookvale.github.io
git pull
git checkout production
rm -rf ./_site
JEKYLL_ENV=production jekyll build
sudo rsync -rv /home/ubuntu/teambrookvale.github.io/_site/ /var/www/teambrookvale.com.au/html/
sudo chown -R www-data:www-data /var/www/teambrookvale.com.au/
