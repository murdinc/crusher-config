# DEV SPEC FILE
# /////////////////////////////////////////////////

NAME = dev

VERSION = 1
REQUIRES = nginx, php, user-aabdo, golang

[PACKAGES]
	apt_get = vim

[CONFIGS]
	debian_root = "/etc/"

[CONTENT]
	source = spec
	# source = git
	# git_command = git clone ...
	debian_root = "/usr/share/nginx/html/"

[COMMANDS]
	pre = ""

	post = "sudo service nginx start, sudo service php5-fpm start, sudo service nginx reload"
