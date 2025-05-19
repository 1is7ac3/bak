function xs --wraps='pacman -Ss' --description 'alias xs=pacman -Ss'
  pacman -Ss $argv
        
end
