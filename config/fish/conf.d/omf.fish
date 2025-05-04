# Path to Oh My Fish install.
set OMF_PATH "$HOME/.local/share/omf"

# Load Oh My Fish configuration.
if test -e "$OMF_PATH/init.fish"
  source "$OMF_PATH/init.fish"
else
  git clone --recursive https://github.com/oh-my-fish/oh-my-fish.git $OMF_PATH
  source "$OMF_PATH/init.fish"
end
