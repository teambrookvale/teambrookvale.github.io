# How to install without WSL:
1. Download and Install a Ruby+Devkit version from RubyInstaller Downloads. Use default options for installation. (https://rubyinstaller.org/downloads/)
2. Open a new command prompt window from the start menu, so that changes to the PATH environment variable becomes effective. Install Jekyll and Bundler via: *gem install jekyll bundler*
3. Check if Jekyll installed properly: *jekyll -v*

# How to install with WSL:
```
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install ruby-full build-essential
sudo gem install jekyll bundler
sudo gem install jekyll-sitemap
sudo gem install jekyll-last-modified-at
sudo gem install wdm
```

# How to start the project if hosted on Windows drive:
```
jekyll serve --livereload --incremental --force_polling```
```

# How to start the project if hosted on WSL or Linux or Mac:
```
jekyll serve --livereload --incremental --watch
```

# 3rd party libraries:
- EmailJS: http://www.emailjs.com/

# Useful links:
- Jekyll: https://jekyllrb.com/docs/
- Jekyll collections: 
	- https://alligator.io/jekyll/collections/
	- https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-collections/
- Liquid: https://shopify.github.io/liquid/