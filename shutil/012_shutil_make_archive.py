import shutil
import os

archive_name = os.path.expanduser(os.path.join('~', 'py', 'shutil', '012'))
#print archive_name
root_dir = os.path.expanduser(os.path.join('~', 'py', 'shutil', '012folder'))
shutil.make_archive(archive_name, 'gztar', root_dir)

