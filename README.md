# asdf-neovim

[Neovim](https://github.com/neovim/neovim) plugin for [asdf](https://github.com/asdf-vm/asdf) version manager.

## Install

```bash
asdf plugin add neovim https://github.com/aniaan/asdf-neovim.git
```

## Use

Check out the [asdf](https://github.com/asdf-vm/asdf) readme for instructions on how to install & manage versions of Neovim.

### Example

```bash
# Show all installable versions
asdf list-all neovim

# Install specific version
asdf install neovim latest
asdf install neovim 0.9.4
asdf install neovim nightly

# Set a version globally (in your ~/.tool-versions file)
asdf global neovim latest

# Set a version locally (in your current directory's .tool-versions file)
asdf local neovim 0.9.4
```
