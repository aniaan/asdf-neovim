import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib import Plugin

PLUGIN = Plugin(
    name="neovim",
    cmd="nvim",
    repo_name="neovim/neovim",
    filename_template=lambda kwargs: f"nvim-{kwargs['platform']}{'-' + kwargs['arch'] if kwargs['platform'] != 'linux64' else ''}",
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
