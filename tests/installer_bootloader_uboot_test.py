import os
from unittest.mock import Mock, patch

# Import test module
import sonic_installer.bootloader.uboot as uboot


@patch("sonic_installer.bootloader.uboot.subprocess.call", Mock())
@patch("sonic_installer.bootloader.uboot.run_command")
def test_remove_image(run_command_patch):
    # Constants
    image_path_prefix = os.path.join(uboot.HOST_PATH, uboot.IMAGE_DIR_PREFIX)
    exp_image_path = f'{image_path_prefix}expeliarmus-{uboot.IMAGE_PREFIX}abcde'

    intstalled_images = [
        f'{uboot.IMAGE_PREFIX}expeliarmus-{uboot.IMAGE_PREFIX}abcde',
        f'{uboot.IMAGE_PREFIX}expeliarmus-abcde',
    ]

    bootloader = uboot.UbootBootloader()
    bootloader.get_installed_images = Mock(return_value=intstalled_images)

    # Verify rm command was executed with image path
    bootloader.remove_image(intstalled_images[0])
    args_list = uboot.subprocess.call.call_args_list
    assert len(args_list) > 0

    args, _ = args_list[0]
    assert exp_image_path in args[0]
