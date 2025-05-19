function re --wraps='sudo pacman -Rsncu $(pacman -Qtdq)' --description 'alias re=sudo pacman -Rsncu $(pacman -Qtdq)'
  sudo pacman -Rsncu $(pacman -Qtdq) $argv
        
end
