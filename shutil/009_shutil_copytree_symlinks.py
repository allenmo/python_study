import shutil

shutil.copytree('009folder', '009folder_cp_symlink_True', symlinks=True)
shutil.copytree('009folder', '009folder_cp_symlink_False', symlinks=False)
