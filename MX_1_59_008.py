import os
# import string
import distutils.dir_util
import distutils.file_util
from fnmatch import fnmatch
import win32file
import sys
import glob
# import time
# import stat
import re
# import itertools

# find the letter of USB
drive_list = []
drivebits = win32file.GetLogicalDrives()
for drive in range(1, 26):
    mask = 1 << drive
    if drivebits & mask:
        # here if the drive is at least there
        drname = '%c:\\' % chr(ord('A') + drive)
        t = win32file.GetDriveType(drname)
        if t == win32file.DRIVE_REMOVABLE:
            drive_list.append(drname)

# convert USB letter to string and use it as a destination for copy
pre_dst = ''.join(drive_list)


''' List of root folders for all parts. Change those links if location is changed '''

# root folder used as root for all Configurations, Products and Content 1.59.008
mx_alma = '\\\\alma\\Images\\Internal images\\Mexico\\1.59.008'

# root folder used as root for all 1.59.006 Content
mx_alma_006 = '\\\\alma\\Images\\Internal images\\Mexico\\1.59.006'

# root folder for Blade Platform
mx_blade = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\blade'

# root folder for Apex (Nevada) Platform
mx_apex = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\nevada'

# root folder for Epson 700 cashier
mx_epson = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\cashier\\epson700'

# root folder for Headless (mediastation) cashier
mx_headless = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\cashier\\headless'

# root folder for Mediastation product. Yes, it is from 1.55 Mexico
mx_mediastation = '\\\\alma\\Images\\Internal images\\Mexico\\1.04.155'

# root folder for Install Script
usb_hdd_install = '\\\\alma\\Projects\\GD\\Automation\\V4.0.3\\USB_HDD_Install'

''' End of list '''


def install():

    distutils.dir_util.copy_tree(usb_hdd_install, pre_dst)
    print('Install script copied to ' + pre_dst)


def mx_terminal_configuration():

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_mexico_terminal_*'

    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['OLD_v3_configuration', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # create full path
                conf.append(fullpath)  # add path to array
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst = pre_dst + '\\configuration'

# copy top 4 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 4:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst)
        print("Copied " + str1 + " to " + dst)
        i += 1


def mx_terminal_product():

    # array of production folders
    pro = []

    pattern = 'terminal_dual_es_*'
    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)
                pro.append(fullpath)
                pro.sort(reverse=True)

# define destination for future copy
    dst = pre_dst + '\\product'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(pro[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst)
        print("Copied " + str1 + " to " + dst)
        i += 1


def mx_content():

    # new folder required for content to be visible by install script.
    full_path = pre_dst + '\\content\\terminal_mexico_Games.000_1.wim'
    if not os.path.exists(full_path):  # checks if it exists and creates it if not.
        os.makedirs(pre_dst + '\\content\\terminal_mexico_Games.000_1.wim')

    # define destination for future copy
    dst = pre_dst + '\\content\\terminal_mexico_Games.000_1.wim'

    # pattern to filter files
    pattern = "*.wim"

    # array with full path to files
    cont = []

    # loop to find all .wim files in "Content" folders and filtering other folders. Results added to cont[] array
    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['configuration', 'product', 'OLD_v3_configuration']]  # ignore folders
        for filename in files:
                if fnmatch(filename, pattern):
                    content_path = os.path.join(path, filename)
                    split_name = content_path.split('\\')[7]
                    build_version = int(split_name)
                    if build_version >= 0o10:
                        cont.append(content_path)
                        cont.sort(reverse=True)

    i = 0
    while i < len(cont):
        str1 = ''.join(cont[i])  # source path in string for future copy
        head, tail = os.path.split(cont[i])  # split full path from array in 2 parts: path (head) and file name (tale)
        if os.path.exists(dst + '\\' + tail):  # if file with "tail" name exists in destination folder -> skip
            print("skip " + tail)
            i += 1
        else:  # otherwise -> copy file
            distutils.file_util.copy_file(str1, dst)
            i += 1
            print('Copied ' + str1 + ' to ' + dst)


def mx_content_006():

    # new folder required for content to be visible by install script.
    full_path = pre_dst + '\\content\\terminal_mexico_Games.000_1.wim'
    if not os.path.exists(full_path):  # checks if it exists and creates it if not.
        os.makedirs(pre_dst + '\\content\\terminal_mexico_Games.000_1.wim')

    # define destination for future copy
    dst = pre_dst + '\\content\\terminal_mexico_Games.000_1.wim'

    # pattern to filter files
    pattern = "*.wim"

    # array with full path to files
    cont = []

    # loop to find all .wim files in "Content" folders and filtering other folders. Results added to cont[] array
    for path, dirs, files in os.walk(mx_alma_006):
        dirs[:] = [d for d in dirs if d not in ['configuration', 'product', 'OLD_configuration', 'new_v5_configuration', 'old_configuration']]  # ignore folders
        files[:] = [f for f in files if f not in ['DummyGames159.wim']]  # ignore files
        for filename in files:
                if fnmatch(filename, pattern):
                    content_path = os.path.join(path, filename)
                    split_name = content_path.split('\\')[7]
                    build_version = int(split_name)
                    if build_version >= 0o10:
                        cont.append(content_path)
                        cont.sort(reverse=True)

    i = 0
    while i < len(cont):
        str1 = ''.join(cont[i])  # source path in string for future copy
        head, tail = os.path.split(cont[i])  # split full path from array in 2 parts: path (head) and file name (tale)
        if os.path.exists(dst + '\\' + tail):  # if file with "tail" name exists in destination folder -> skip
            print("skip " + tail)
            i += 1
        else:  # otherwise -> copy file
            distutils.file_util.copy_file(str1, dst)
            i += 1
            print('Copied ' + str1 + ' to ' + dst)


def mx_banners():

    dst_banners = pre_dst + '\\content'

    src_banners_spa = '\\\\alma\\Production\\Production_prototype_2012\\0_storage\\generic\\terminal_banners.generic.ENG.3_1.wim'
    src_banners_eng = '\\\\alma\\Production\\Production_prototype_2012\\0_storage\\generic\\terminal_banners.generic.SPA.3_1.wim'
    src_banners_spa_promo = '\\\\alma\\production\\Production_prototype_2012\\0_storage\\generic\\promo\\terminal_banners.promo.SPA.1_1.wim'

    distutils.file_util.copy_file(src_banners_spa, dst_banners)
    distutils.file_util.copy_file(src_banners_eng, dst_banners)
    distutils.file_util.copy_file(src_banners_spa_promo, dst_banners)


def mx_platform_blade():

    mx_blade_list = []  # initial list will all files

    dst = pre_dst + '\\platform'  # destination for copy

    pattern = 'terminal_mxblade_*.*'
    files = glob.glob1(mx_blade, pattern)  # find all files that fit the pattern
    mx_blade_list.append(files)  # add those files in the list
    str1 = ' '.join(mx_blade_list[0])  # convert list to string
    p = re.compile('\w+\d.\d\d')  # look though string files that fit this pattern with numbers
    m = p.findall(str1)  # find files using the constructor above
    m1 = max(m)  # find the biggest number
    str2 = ''.join(m1)  # convert list to string
    path1 = mx_blade + '\\' + str2 + '.wim'  # prepare full path to copy .wim file
    path2 = mx_blade + '\\' + str2 + '.md5'  # prepare full path to copy .md5 file
    distutils.file_util.copy_file(path1, dst)  # copy file
    print('Copied ' + str2 + '.wim' + ' to ' + dst)
    distutils.file_util.copy_file(path2, dst)
    print('Copied ' + str2 + '.md5' + ' to ' + dst)


def mx_platform_apex():

    mx_apex_list = []

    dst = pre_dst + '\\platform'

    pattern = 'terminal_nevada_*.*'
    files = glob.glob1(mx_apex, pattern)  # find all files that fit the pattern
    mx_apex_list.append(files)  # add those files in the list
    str1 = ' '.join(mx_apex_list[0])  # convert list to string
    p = re.compile('\w+\d.\d\d')  # look though string files that fit this pattern with numbers
    m = p.findall(str1)  # find files using the constructor above
    m1 = max(m)  # find the biggest number
    str2 = ''.join(m1)  # convert list to string
    path1 = mx_apex + '\\' + str2 + '.wim'  # prepare full path to copy .wim file
    path2 = mx_apex + '\\' + str2 + '.md5'  # prepare full path to copy .md5 file
    distutils.file_util.copy_file(path1, dst)  # copy file
    print('Copied ' + str2 + '.wim' + ' to ' + dst)
    distutils.file_util.copy_file(path2, dst)
    print('Copied ' + str2 + '.md5' + ' to ' + dst)


def mx_cashier_platform():

    mx_epson_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'cashier_epson700_*'

    for file in glob.glob1(mx_epson, pattern):
        platform_path = os.path.join(mx_epson, file)
        mx_epson_list.append(platform_path)
        mx_epson_list.sort(reverse=True)

    i = 0
    while i != 2:
        platform_str = ''.join(mx_epson_list[i])  # converts list to string
        distutils.file_util.copy_file(platform_str, dst_platform)
        print('Copied ' + platform_str + ' to ' + dst_platform)
        i += 1


def mx_cashier_configuration():

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_cashier_epson700_*'

    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['OLD_v3_configuration', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # create full path
                conf.append(fullpath)  # add full path to array
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst = pre_dst + '\\configuration'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst)
        print("Copied " + str1 + " to " + dst)
        i += 1


def mx_cashier_product():

    pro_cashier = []  # array of production folders

    pattern = 'cashier_*'

    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)
                pro_cashier.append(fullpath)
                pro_cashier.sort(reverse=True)

# define destination for future copy
    dst = pre_dst + '\\product'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(pro_cashier[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst)
        print("Copied " + str1 + " to " + dst)
        i += 1

'''
def mx_mediastation_platform():

    mx_headless_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'mediastation_headlessmedia_*'

    for file in glob.glob1(mx_headless, pattern):
        platform_path = os.path.join(mx_headless, file)
        mx_headless_list.append(platform_path)
        mx_headless_list.sort(reverse=True)

    i = 0
    while i != 2:
        platform_str = ''.join(mx_headless_list[i])  # converts list to string
        distutils.file_util.copy_file(platform_str, dst_platform)
        print('Copied ' + platform_str + ' to ' + dst_platform)
        i += 1
'''


def mx_mediastation_platform():

    mx_headless_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'mediastation_headlessmedia_3.*.*_f1*'

    for file in glob.glob1(mx_headless, pattern):
        platform_path = os.path.join(mx_headless, file)
        mx_headless_list.append(platform_path)
        mx_headless_list.sort(reverse=True)

    # copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        platform_str = ''.join(mx_headless_list[i])  # converts list to string
        distutils.file_util.copy_file(platform_str, dst_platform)
        print('Copied ' + platform_str + ' to ' + dst_platform)
        i += 1


def mx_mediastation_configuration():

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_mediastation_*'

    for path, dirs, files in os.walk(mx_alma):
        dirs[:] = [d for d in dirs if d not in ['OLD_v3_configuration', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # create full path
                conf.append(fullpath)  # add full path to array
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst = pre_dst + '\\configuration'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst)
        print("Copied " + str1 + " to " + dst)
        i += 1


def mx_mediastation_product():

    mx_media_product_list = []

    dst_media_product = pre_dst + '\\product'

    pattern = 'mediastation_*'

    for path, dirs, files in os.walk(mx_mediastation):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)
                mx_media_product_list.append(fullpath)
                mx_media_product_list.sort(reverse=True)

    # copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        mx_media_str = ''.join(mx_media_product_list[i])  # converts list to string
        distutils.file_util.copy_file(mx_media_str, dst_media_product)
        print('Copied ' + mx_media_str + ' to ' + dst_media_product)
        i += 1


def mx_mediastation_cert_fix():
    src_fix = '\\\\alma\\Public2\\Aleksandr_s\\certupdate\\certupdate.exe'

    distutils.file_util.copy_file(src_fix, pre_dst)
    print('Copied ' + src_fix + ' to ' + pre_dst)


if drive_list:
    print('------------------------------------------------------------------------------------')
    print('The year 2016 ... ')
    print('')
    print(' _____ _____ __ __ _____ _____ _____    ___     ___ ___   ___ ___ ___ ')
    print('|     |   __|  |  |     |     |     |  |_  |   |  _| . | |   |   | . |')
    print('| | | |   __|-   -|-   -|   --|  |  |   _| |_ _|_  |_  |_| | | | | . |')
    print('|_|_|_|_____|__|__|_____|_____|_____|  |_____|_|___|___|_|___|___|___|')
    print('                                                   With the Vengeance ')
    print('------------------------------------------------------------------------------------')
    choice = ''
    while choice != '5':
        print('Install script v4.0.3 will be copied with any choice')
        choice = input("[1] - if you would like to copy TERMINAL part only: "
                       "\n[2] - if you would like to copy CASHIER part only: "
                       "\n[3] - if you would like to copy MEDIASTATION part only: "
                       "\n[4] - if you would like to copy EVERYTHING: "
                       "\n[5] - if you would like to Exit"
                       "\nPlease type your choice: ")
        if choice == '1':
            print('Preparing to copy terminal part ...')
            # install script
            install()
            # terminal
            mx_platform_apex()
            mx_platform_blade()
            mx_terminal_product()
            mx_terminal_configuration()
            mx_content()
            mx_content_006()
            mx_banners()
            sys.exit()
        if choice == '2':
            print('Preparing to copy cashier part')
            # install script
            install()
            # cashier
            mx_cashier_platform()
            mx_cashier_product()
            mx_cashier_configuration()
            sys.exit()
        if choice == '3':
            print('Preparing to copy mediastation part')
            # install script
            install()
            # mediastation
            mx_mediastation_product()
            mx_mediastation_configuration()
            mx_mediastation_platform()
            mx_mediastation_cert_fix()
            sys.exit()
        if choice == '4':
            print('Preparing to copy EVERYTHING')
            # install script
            install()
            # terminal
            mx_terminal_configuration()
            mx_terminal_product()
            mx_content()
            mx_content_006()
            mx_banners()
            mx_platform_blade()
            mx_platform_apex()
            # cashier
            mx_cashier_platform()
            mx_cashier_product()
            mx_cashier_configuration()
            # mediastation
            mx_mediastation_product()
            mx_mediastation_platform()
            mx_mediastation_configuration()
            mx_mediastation_cert_fix()
            sys.exit()
        elif choice == "5":
            sys.exit()
else:
    input('USB not found. Press Enter to exit')
    sys.exit()
