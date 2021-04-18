if exists('g:remote_copy_loaded') || &compatible
    finish
endif


if !has('python3')
    echohl Error
    echomsg "remote-copy.vim requires Vim compiled with Python3."
    echohl None
    " stop sourcing this script
    finish
end


let g:remote_copy_loaded = 1

vmap <C-c> y:call remote_copy#copy2clipboard(getreg('"'))<cr>
