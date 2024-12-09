import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from lib.lib import Plugin

PLUGIN = Plugin(
    name="neovim",
    cmd="nvim",
    repo_name="neovim/neovim",
    filename_template=lambda kwargs: f"nvim-{kwargs['platform']}{'' if kwargs['platform'] == 'linux64' else f'-{kwargs['arch']}'}.tar.gz",
    platform_map={
        "darwin": "macos",
        "linux": "linux64",
    },
    arch_map={
        "x86_64": "x86_64",
        "aarch64": "arm64",
    },
    checksum_filename_template="{filename}.sha256sum",
    bin_path=lambda kwargs: f"{kwargs['filename'].rstrip('.tar.gz')}/bin/nvim",
    recover_raw_version=lambda x: f"v{x}" if x[0].isdigit() else x,
)
