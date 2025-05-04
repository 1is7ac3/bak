function dnflist --wraps='dnf list \\*$argv\\*' --description 'alias dnflist=dnf list \\*$argv\\*'
  dnf list \*$argv\*
        
end
