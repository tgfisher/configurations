# Prep

Some environment variables need to be added to ~/.bashrc or ~/.zshrc:

```bash
export CONFIG_REPO=<path>/<to>/<this>/<repo>
```

This repo has **submodules**. If this is a fresh setup you need to `init`. If
changes have been made in another location then `update` is required to fetch
the current data.

```bash
git submodule init
git submodule update
```

# Tmux

Window manager.

```bash
mkdir ~/.config/tmux
ln -s $CONFIG_REPO/tmux.common ~/.config/tmux/tmux.conf # if this is a laptop then `tmux.laptop`
```

# Nvim

A good configurable editor

```bash
ln -s $CONFIG_REPO/ksnvim ~/.config/nvim
```


# Vim

A good simpler editor


