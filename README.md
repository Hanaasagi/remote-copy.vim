# remote-copy.vim

Copy the text in remote Vim to local clipboard. It depends on OSC52 escape sequences.
Unlike other OSC52 Vim scripts (e.g. [code snippet in chromium hterm][g]), it solves the flash problem when copy the text.

## Requirements

- Vim 7.3 or higher.
- Python3+.
- Terminal that supported OSC52 escape sequences.
- Tmux 3.3 and above: Add `set -g allow-passthrough on` in tmux config.


## Installation

You can install this plugin via Vim plugin managers. Then add following code in your `vimrc`.

```Vim
vmap <C-c> y:call remote_copy#copy2clipboard(getreg('"'))<cr>
```


### [Vundle][v]

```vim
Plugin 'Hanaasagi/remote-copy.vim'
```

### [Pathogen][p]

```sh
git clone --depth=1 https://github.com/Hanaasagi/remote-copy.vim ~/.vim/bundle/remote-copy.vim
```

### [vim-plug][vp]

```vim
Plugin 'Hanaasagi/remote-copy.vim'
```

## License

BSD 3-Clause License

Copyright (c) 2021, 秋葉
All rights reserved.

[g]: https://chromium.googlesource.com/apps/libapps/+/master/hterm/etc/osc52.vim#93
[v]: https://github.com/gmarik/vundle
[p]: https://github.com/tpope/vim-pathogen
[vp]: https://github.com/junegunn/vim-plug
