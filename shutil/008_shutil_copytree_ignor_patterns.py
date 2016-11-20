import shutil

shutil.copytree('008folder', '008folder_cp', ignore=shutil.ignore_patterns('*.tmp'))

