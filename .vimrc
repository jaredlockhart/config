set ruler
set nu
set ts=2
set sw=2
set autoindent
set expandtab
set autoread
syntax on
set nobackup
set nowritebackup
set noswapfile
set mouse=a
au BufNewFile,BufRead *.less set filetype=less
set tabpagemax=50
autocmd BufWritePre *.* :%s/\s\+$//e
autocmd BufRead,BufNewFile *.jsm set filetype=javascript
