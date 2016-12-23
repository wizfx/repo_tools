# colors
####################################
col_reset=$'\e[0;37m'
red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'

# system aliases
####################################
alias cls="clear"
alias ..="cd ../"
alias ll="clear ; ls -a1X --group-directories-first"
alias l=ll

alias o="explorer ."

# reload this file
####################################
alias src="source ~/.bashrc ; clear ; printf 'sourcing ~/.bashrc'"
alias reloadalias=". ~/.bashrc ; printf 'alias reloaded'"

# project aliases
####################################
currentProjectPath="/d/depot/cosmos_4.13/"
cosmosPath="/d/depot/cosmos_4.13"
hampPath="/d/depot/VLUnrealApp_ported_4.12.3"
alias project="cd $currentProjectPath"
alias projhamp="cd $hampPath"
alias projcosmos="cd $cosmosPath"
alias launchhamp="nohup D:/depot/VLUnrealApp_ported_4.12.3/Engine/Binaries/Win64/UE4Editor.exe 'D:depot/VLUnrealApp_ported_4.12.3/VLUnreal/VLUnreal.uproject' &>/dev/null &"
alias launchcosmos="nohup D:/depot/cosmos_4.13/Engine/Binaries/Win64/UE4Editor.exe 'D:/depot/cosmos_4.13/VLUnreal/VLUnreal.uproject' &>/dev/null &"
alias launch="nohup D:/depot/cosmos_4.13/Engine/Binaries/Win64/UE4Editor.exe 'D:/depot/cosmos_4.13/VLUnreal/VLUnreal.uproject' &>/dev/null &"

# git aliases
####################################
alias gs=getStatus
alias fetchstatus=getStatus

# funzone
####################################
alias foo="reloadAliases"

# do work
####################################
function printCommands {
  printf "\n\n"
  printf "some bash commands:\n"
  printf " ${grn}src ${col_reset}= reload alias file which is located: ~\\.bashrc\n"
  # printf " ${grn}gs ${col_reset}= git fetch and git status\n"
  printf "\n"
  printf " ${grn}project ${col_reset}= cd to latest project path, which is: "
  echo $currentProjectPath
  printf "\n"
  printf " ${grn}launch ${col_reset}= launch unreal to the latest project\n"
  printf "\n"
  printf " ${grn}projhamp ${col_reset}= cd to project path, which is: D:/depot/VLUnrealApp_ported_4.12.3\n"
  printf " ${grn}projcosmos ${col_reset}= cd to project path, which is: D:/depot/cosmos_4.13\n"
  printf " ${grn}launchhamp ${col_reset}= launch VLUnreal Hampden App\n"
  printf " ${grn}launchcosmos ${col_reset}= launch VLUnreal Cosmos App\n"
  printf "\n\n"
}

function navigate ()
{
    printf "$1"
    printf "fool"
    printf "$2"

}

function reloadAliases {
  configFile=". ~/.bashrc"
  configFile
  #clear
  printf "sourcing "configFile
}

function getStatus {
  # project
  clear
  printf "${cyn}\n\n\n\nfetching from git repo..."
  git fetch
  clear
  printf "\ncurrent branch:\n\n"
  git branch -a
  printf "\n${cyn}current status:\n${col_reset}\n"
  git status
  printCommands
}
