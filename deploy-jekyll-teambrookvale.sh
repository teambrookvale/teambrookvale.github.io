#!/bin/bash
# Install Ruby Gems to ~/gems
rsync --recursive --delete /var/www/teambrookvale.com.au/html/ /home/ubuntu/teambrookvale.github.io/_site_backup/ 
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
cd /home/ubuntu/teambrookvale.github.io
git reset --hard
git checkout production
git pull
rm -rf ./_site
JEKYLL_ENV=production jekyll build
sudo rsync --recursive --delete --delete-excluded --exclude 'deploy-jekyll-teambrookvale.sh' --exclude 'Jenkinsfile' --exclude 'README.md' /home/ubuntu/teambrookvale.github.io/_site/ /var/www/teambrookvale.com.au/html/
sudo chown -R www-data:www-data /var/www/teambrookvale.com.au/
