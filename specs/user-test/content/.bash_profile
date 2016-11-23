# bring in the dev server data by default

export EDITOR=vim

export GOPATH=~/go

export PATH=$PATH:/sbin:/usr/sbin:$GOPATH/bin

alias vi=vim
alias ls="ls -Alh --color=auto --group-directories-first"

export LS_COLORS="no=00:fi=00:di=00;36:ln=00;34:pi=40;33:so=00;35:bd=40;33;01:cd=40;33;01:or=01;05;37;41:mi=01;05;37;41:ex=00;32:*.cmd=00;32:*.exe=00;32:*.com=00;32:*.btm=00;32:*.bat=00;32:*.sh=00;32:*.csh=00;32:*.tar=00;31:*.tgz=00;31:*.arj=00;31:*.taz=00;31:*.lzh=00;31:*.zip=00;31:*.z=00;31:*.Z=00;31:*.gz=00;31:*.bz2=00;31:*.bz=00;31:*.tz=00;31:*.rpm=00;31:*.cpio=00;31:*.jpg=00;35:*.gif=00;35:*.bmp=00;35:*.xbm=00;35:*.xpm=00;35:*.png=00;35:*.tif=00;35:"

alias p='pushd'
alias o='popd'

if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# Keep our path through a sudo
alias sudo='sudo env PATH=$PATH EDITOR=vim'
alias su='su -p'

function git_branch {
    local __user_and_host="\[\033[01;31m\]\u@\h"
    local __cur_location="\[\033[01;34m\]\w"
    local __git_branch_color="\[\033[1;34m\]"
    local __git_branch=' `git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\/`'
    local __prompt_tail="\[\033[01;00m\]$"
    local __last_color="\[\033[00m\]"
    export PS1="$__user_and_host\[\033[00m\]:$__cur_location$__git_branch_color$__git_branch$__prompt_tail$__last_color "
}
git_branch
