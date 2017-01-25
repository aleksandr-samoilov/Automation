import os
import string
import distutils.dir_util
import distutils.file_util
from fnmatch import fnmatch
import win32file
import sys
import glob

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

# root folder used as root for all Configurations, Products and Content
pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

# root folder for Lara Platform
pr_lara = '\\\\alma\Images\\Internal images\GD\\Platforms\\terminal\\lara'

# root folder for Blade Platform
pr_blade = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\puertorico'

# root folder for Silverball Platform
pr_silverball = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\puertorico'

# root folder for Partnertech 6200 cashier
pr_partnertech = '\\\\alma\\Images\\Internal images\\GD\\Platforms\cashier\\partnertech'

# root folder for Headless (mediastation) cashier platform
pr_headless = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\cashier\\headless'

# root folder for Mediastation product. Yes, it is from 1.55 Mexico
pr_media_product = '\\\\alma\\Images\\Internal images\\Mexico\\1.04.155'

# root folder for Install Script
usb_hdd_install = '\\\\alma\\Projects\\GD\\Automation\\V4.0.3\\USB_HDD_Install'

''' End of list '''


def install():
    # usb_hdd_install = '\\\\alma\\Projects\\GD\\Automation\\V4.0.3\\USB_HDD_Install'

    distutils.dir_util.copy_tree(usb_hdd_install, pre_dst)
    print('Install script copied to ' + pre_dst)


def pr_configuration():
    # root folder
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_puertorico_terminal_*'

    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # filename)
                conf.append(fullpath)
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst1 = pre_dst + '\\configuration'

# copy top 8 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 8:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst1)
        print("Copied " + str1 + " to " + dst1)
        i += 1


def pr_cashier_configuration():
    # root folder
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_cashier_partnertech6200_*'

    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # filename)
                conf.append(fullpath)
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst1 = pre_dst + '\\configuration'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst1)
        print("Copied " + str1 + " to " + dst1)
        i += 1


def pr_mediastation_configuration():
    # root folder
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    # array of config folders
    conf = []

    # pattern to filter out other files
    pattern = 'vbqa_mediastation*'

    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'product']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):  # find all files that fit the pattern
                fullpath = os.path.join(path, filename)  # filename)
                conf.append(fullpath)
                conf.sort(reverse=True)  # reverse the list

# define source and destination for future copy
    dst1 = pre_dst + '\\configuration'

# copy top 2 files (those will be terminal configuration files. Most likely). Change to lower number in case of problems
    i = 0
    while i != 2:
        str1 = ''.join(conf[i])  # converts list to string
        distutils.file_util.copy_file(str1, dst1)
        print("Copied " + str1 + " to " + dst1)
        i += 1


def pr_product():
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    pro = []  # array of production folders

    pattern = 'terminal_single_es*'
    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)  # filename)
                pro.append(fullpath)
                pro.sort(reverse=True)

# converts path to string

    str2 = ''.join(pro[0])

# define destination for future copy
    dst2 = pre_dst + '\\product'

# copy all files
    distutils.file_util.copy_file(str2, dst2)
    print("Copied " + str2 + " to " + dst2)


def pr_cashier_product():
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    pro_cashier = []  # array of production folders

    pattern = 'cashier_*'

    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)
                pro_cashier.append(fullpath)
                pro_cashier.sort(reverse=True)

# converts path to string
    str2 = ''.join(pro_cashier[0])

# define destination for future copy
    dst2 = pre_dst + '\\product'

# copy all files
    distutils.file_util.copy_file(str2, dst2)
    print("Copied " + str2 + " to " + dst2)


def pr_content():
    # root folder to work with
    # pr_alma = '\\\\alma\\Images\\Internal images\\Puertorico\\1.04.156'

    # new folder required for content to be visible by install script.
    full_path = pre_dst + '\\content\\terminal_puertorico_Games.000_1.wim'
    if not os.path.exists(full_path):  # checks if it exists and creates it if not.
        os.makedirs(pre_dst + '\\content\\terminal_puertorico_Games.000_1.wim')

    # define destination for future copy
    dst3 = pre_dst + '\\content\\terminal_puertorico_Games.000_1.wim'

    # pattern to filter files
    pattern = "*.wim"

    # array with full path to files
    cont = []

    # loop to find all .wim files in "Content" folders and filtering other folders. Results added to cont[] array
    for path, dirs, files in os.walk(pr_alma):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'configuration', 'product', '410v2',
                                                '454']]  # ignore folders
        files[:] = [f for f in files if f not in ['Banners_wmv_promo.wim']]  # ignore files
        for filename in files:
                if fnmatch(filename, pattern):
                    content_path = os.path.join(path, filename)
                    split_name = content_path.split('\\')[7]
                    build_version = int(split_name)
                    if build_version >= 411:
                        cont.append(content_path)
                        cont.sort(reverse=True)

    i = 0
    while i < len(cont):
        str3 = ''.join(cont[i])  # source path in string for future copy
        head, tail = os.path.split(cont[i])  # split full path from array in 2 parts: path (head) and file name (tale)
        if os.path.exists(dst3 + '\\' + tail):  # if file with "tail" name exists in destination folder -> skip
            print("skip " + tail)
            i += 1
        else:  # otherwise -> copy file
            distutils.file_util.copy_file(str3, dst3)
            i += 1
            print('Copied ' + str3 + ' to ' + dst3)


def pr_banners():

    dst_banners = pre_dst + '\\content'

    src_banners_spa = '\\\\alma\\Production\\Production_prototype_2012\\0_storage\\generic\\terminal_banners.generic.ENG.3_1.wim'
    src_banners_eng = '\\\\alma\\Production\\Production_prototype_2012\\0_storage\\generic\\terminal_banners.generic.SPA.3_1.wim'
    src_banners_spa_promo = '\\\\alma\\production\\Production_prototype_2012\\0_storage\\generic\\promo\\terminal_banners.promo.SPA.1_1.wim'

    distutils.file_util.copy_file(src_banners_spa, dst_banners)
    distutils.file_util.copy_file(src_banners_eng, dst_banners)
    distutils.file_util.copy_file(src_banners_spa_promo, dst_banners)


def pr_platform_lara():
    # pr_lara = '\\\\alma\Images\\Internal images\GD\\Platforms\\terminal\\lara'

    pr_lara_list = []

    dst_platform = pre_dst + '\\platform'

    for path, dirs, files in os.walk(pr_lara):
        for filename in files:
            if filename.endswith('.wim'):
                platform_path = os.path.join(path, filename)
                pr_lara_list.append(platform_path)
                pr_lara_list.sort(key=lambda x: os.stat(os.path.join(platform_path, x)).st_ctime, reverse=True)

    platform_str = ''.join(pr_lara_list[0])

    distutils.file_util.copy_file(platform_str, dst_platform)

    print('Copied ' + platform_str + ' to ' + dst_platform)


def pr_platform_blade():
    # pr_blade = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\puertorico'

    pr_blade_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'terminal_blade_*.wim'

    for file in glob.glob1(pr_blade, pattern):
        platform_path = os.path.join(pr_blade, file)
        pr_blade_list.append(platform_path)
        pr_blade_list.sort(reverse=True)

    platform_str = ''.join(pr_blade_list[0])

    distutils.file_util.copy_file(platform_str, dst_platform)

    print('Copied ' + platform_str + ' to ' + dst_platform)


def pr_platform_silverball():
    # pr_silverball = '\\\\alma\\Images\\Internal images\\GD\\Platforms\\terminal\\puertorico'

    pr_silverball_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'terminal_silverball_*.wim'

    for file in glob.glob1(pr_silverball, pattern):
        platform_path = os.path.join(pr_silverball, file)
        pr_silverball_list.append(platform_path)
        pr_silverball_list.sort(reverse=True)

    platform_str = ''.join(pr_silverball_list[0])

    distutils.file_util.copy_file(platform_str, dst_platform)

    print('Copied ' + platform_str + ' to ' + dst_platform)


def pr_cashier_platform():
    # pr_partnertech = '\\\\alma\\Images\\Internal images\\GD\\Platforms\cashier\\partnertech'

    pr_partnertech_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'cashier_partnertech6200_*'

    for file in glob.glob1(pr_partnertech, pattern):
        platform_path = os.path.join(pr_partnertech, file)
        pr_partnertech_list.append(platform_path)
        pr_partnertech_list.sort(reverse=True)

    platform_str = ''.join(pr_partnertech_list[0])

    distutils.file_util.copy_file(platform_str, dst_platform)

    print('Copied ' + platform_str + ' to ' + dst_platform)


def pr_mediastation_platform():

    pr_headless_list = []

    dst_platform = pre_dst + '\\platform'

    pattern = 'mediastation_headlessmedia_*'

    for file in glob.glob1(pr_headless, pattern):
        platform_path = os.path.join(pr_headless, file)
        pr_headless_list.append(platform_path)
        pr_headless_list.sort(reverse=True)

    platform_str = ''.join(pr_headless_list[0])

    distutils.file_util.copy_file(platform_str, dst_platform)

    print('Copied ' + platform_str + ' to ' + dst_platform)


def pr_mediastation_product():

    pr_media_product_list = []

    dst_media_product = pre_dst + '\\product'

    pattern = 'mediastation_*'

    for path, dirs, files in os.walk(pr_media_product):
        dirs[:] = [d for d in dirs if d not in ['ignore_500', 'ignore', 'content', 'configuration']]  # ignore folders
        for filename in files:
            if fnmatch(filename, pattern):
                fullpath = os.path.join(path, filename)
                pr_media_product_list.append(fullpath)
                pr_media_product_list.sort(reverse=True)

    pr_media_str = ''.join(pr_media_product_list[0])

    distutils.file_util.copy_file(pr_media_product_list, dst_media_product)

    print('Copied ' + pr_media_str + ' to ' + dst_media_product)

if drive_list:
    print('------------------------------------------------------------------------------------')
    print('The year 2011 ... ')
    print('')
    print(' _____  _     _ _______   ______  _______  _____        ______ _____ _______  _____ ')
    print('|_____] |     | |______  |_____/     |    |     |      |_____/   |   |       |     |')
    print('|       |_____| |______  |    \_     |    |_____|      |    \__ _|__ |_____  |_____|')
    print('')
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
            pr_platform_silverball()
            pr_platform_blade()
            pr_platform_lara()
            pr_product()
            pr_configuration()
            pr_content()
            pr_banners()
            sys.exit()
        if choice == '2':
            print('Preparing to copy cashier part')
            # install script
            install()
            # cashier
            pr_cashier_platform()
            pr_cashier_product()
            pr_cashier_configuration()
            sys.exit()
        if choice == '3':
            print('Preparing to copy mediastation part')
            # install script
            # install()
            # mediastation
            pr_mediastation_product()
            # pr_mediastation_configuration()
            # pr_mediastation_platform()
            sys.exit()
        if choice == '4':
            print('Preparing to copy EVERYTHING')
            # install script
            install()
            # terminal
            pr_platform_silverball()
            pr_platform_blade()
            pr_platform_lara()
            pr_product()
            pr_configuration()
            pr_content()
            pr_banners()
            # cashier
            pr_cashier_platform()
            pr_cashier_product()
            pr_cashier_configuration()
            # mediastation
            pr_mediastation_product()
            pr_mediastation_configuration()
            pr_mediastation_platform()
            sys.exit()
        elif choice == "5":
            sys.exit()
else:
    input('USB not found. Press Enter to exit')
    sys.exit()
