# Prep

Some environment variables need to be added to ~/.bashrc or ~/.zshrc:

```
CONFIG_REPO=<path>/<to>/<this>/<repo>
```

# Tmux

Window manager.

```
mkdir ~/.config/tmux
ln -s $CONFIG_REPO/tmux.common ~/.config/tmux/tmux.conf # if this is a laptop then `tmux.laptop`
```

# Nvim

A good configurable editor

```
ln -s $CONFIG_REPO/ksnvim ~/.config/nvim
```


# Vim

A good simpler editor


