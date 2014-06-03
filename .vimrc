set ts=2
set sw=2
set autoindent
set expandtab
syntax on
set nobackup
set nowritebackup
set noswapfile
set mouse=a
au BufNewFile,BufRead *.less set filetype=less
set tabpagemax=50
autocmd BufWritePre *.py :%s/\s\+$//e
