# WEBSERVER SPEC FILE
# /////////////////////////////////////////////////

NAME = hello_world

VERSION = 1
REQUIRES = nginx, php

[PACKAGES]
	# NONE

[CONFIGS]
	debian_root = "/etc/"

[CONTENT]
	source = spec
	# source = git
	# git_command = git clone ...
	debian_root = "/var/www/html/"

[COMMANDS]

	post = "sudo service nginx start, sudo service php7.0-fpm start, sudo service nginx reload"

