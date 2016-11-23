# USER TEST SPEC FILE
# /////////////////////////////////////////////////

NAME = user-test

VERSION = 1
REQUIRES = ""

[PACKAGES]
	apt_get = git

[CONFIGS]
	debian_root = "/etc/"

[CONTENT]
	source = spec
	# source = git
	# git_command = git clone ...
	debian_root = "/home/test/"

[COMMANDS]
	pre = "id -u test &>/dev/null || sudo adduser --disabled-password --gecos '' test, sudo mkdir -p /home/test/.ssh, sudo adduser test sudo"
    post = "sudo chown -R test:test /home/test"

