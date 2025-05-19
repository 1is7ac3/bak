function xr --wraps='sudo pacman -Rsncu' --description 'alias xr=sudo pacman -Rsncu'
  sudo pacman -Rsncu $argv
        
end
