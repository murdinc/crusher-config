# CRUSHER_BASE SPEC FILE
# /////////////////////////////////////////////////

NAME = crusher_base

VERSION = 1
REQUIRES =

[PACKAGES]

[CONFIGS]

[CONTENT]

[COMMANDS]
	pre = "/sbin/parted /dev/xvdf mkpart primary ext4 0% 100%,
	/sbin/mkfs.ext4 /dev/xvdf1,
	mount | grep ' /mnt/crusher' || echo "/dev/xvdf1 /mnt/crusher ext4 defaults 0 0" | sudo tee -a /etc/fstab; sudo mount /mnt/crusher"

	post = "sudo service nginx start, sudo service php7.0-fpm start, sudo service nginx reload"

