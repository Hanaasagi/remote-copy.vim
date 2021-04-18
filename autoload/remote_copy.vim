if exists('g:remote_copy#loaded')
    finish
else
    let g:remote_copy#loaded = 1
endif


let g:rcp_py = "py3 "
exec g:rcp_py "import vim, sys, os, re, os.path"
exec g:rcp_py "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec g:rcp_py "sys.path.insert(0, os.path.join(cwd, 'lib', 'python'))"


function! remote_copy#copy2clipboard(name)
    exec g:rcp_py "from remote_copy import copy2clipboard"
    " syntax error will occurr when newline is existed, so using the doc string.
    exec g:rcp_py printf("copy2clipboard('''%s''')", escape(a:name, "'\"\\"))
    redraw!
endfunction
