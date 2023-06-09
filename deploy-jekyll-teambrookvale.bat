ssh -i %USERPROFILE%\.ssh\ec2-key-pair.pem ubuntu@teambrookvale.com.au "cd /home/ubuntu/teambrookvale.github.io && git checkout production && git pull  && ./deploy-jekyll-teambrookvale.sh"
timeout 20