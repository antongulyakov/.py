
" ===================
" 1. GENERIC SETTINGS
" ===================
set nocompatible " disable vi compatibility mode
set hidden " hide buffers instead of closing them
set history=1000 " increase history size
"
" =================
" 2. VUNDLE PLUGINS
" =================
" Init Vundle
filetype off

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

	Plugin 'VundleVim/Vundle.vim'	" let Vundle manage Vundle, required
	Plugin 'scrooloose/nerdtree'	"A tree explorer plugin for vim

" Finish Vundle initialization
call vundle#end() 

filetype plugin indent on


" ================
" 3. FILE SETTINGS
" ================
"
" " As stated by thousands of people... we aren't in the 70s anymore.
" " If you need to track the changes you do to your files, use Git.
 set noswapfile " disable swap
 set nobackup " disable backup
"
" " Modify indenting settings
 set autoindent " autoindent always ON. 
 set expandtab " expand tabs
 set shiftwidth=4 " spaces for autoindenting
 set tabstop=4 
 set softtabstop=4 " remove a full pseudo-TAB when i press <BS>
"
" " Modify some other settings about files
 set encoding=utf-8 " always use unicode (god damnit, windows)
 set backspace=indent,eol,start " backspace always works on insert mode


" ===============
" 4. COLORS AND UI
" ================
 " " Are we supporting colors?
 " if &t_Co > 2 || has("gui_running")
 "  syntax on
 "
 "   " Show legcy color column at 80 characters.
 "    " TODO: Push the color column at 120 characters when Java is detected.
 "     " (and maybe do the same with other languages such as C#?)
 "      set colorcolumn=80
 "      endif
 "
 "      " Are we supporting a full color pallete?
 "      if &t_Co >= 256 || has("gui_running")
 "       colorscheme Benokai " monokai trends change, you know ^_^
 "       endif
 "
set showmode " always show which more are we in
set wildmenu " enable visual wildmenu

set nowrap " don't wrap long lines
set number " show line numbers
"set relativenumber " show numbers as relative by default
set cursorline " highlight line where the cursor is
set showmatch " higlight matching parentheses and brackets

set linespace=1 " slight linespacing

