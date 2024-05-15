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

This tmux config uses **tpm**. Add this repo before starting a tmux session.

```bash
git clone git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

```bash
cd $CONFIG_REPO/tmux
chmod u+x choose_conf.sh
./choose_conf.sh tmux.leader_<your_choice>
ln -s $CONFIG_REPO/tmux ~/.config/tmux
```

# Nvim

A good configurable editor

```bash
ln -s $CONFIG_REPO/ksnvim ~/.config/nvim
```


# Vim

A good simpler editor


