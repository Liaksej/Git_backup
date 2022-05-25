import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# sourse ['"C:\\My Documents"']
# Exsmple on Mac OS x and Linux:
sourse = ['/Users/aliakseitarusau/Downloads/myfoldr']
# Notice we have to use double quotes inside a string
# for names with spaces in  it. We could have also used
# a raw string by writting [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory
# Example in Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/aliakseitarusau/Downloads/backup'
# Remember to change this to wich folder you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # make directory

# 5. We use the zip command to put the filies in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(sourse))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
    print('Backup FAILED')
    print('Backup FAILED')
    print('Backup FAILED')

