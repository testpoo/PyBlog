# coding=utf-8

import os

print("1.连接网络 2.更新系统时间 3.建立硬盘分区 4.切换软件源 5.安装系统 6.配置系统 7.创建用户")
num = int(input("请输入选项："))
if num == 1:
    try:
        os.popen("iwctl")
        os.popen("station wlp1s0 connect Nokia")
    except Exception as e:
        print("连接网络失败:"+e)
    finally:
        archinstall()
elif num == 2:
    try:
        os.popen("timedatectl set-ntp true")
    except Exception as e:
        print("更新系统时间失败:"+e)
    finally:
        archinstall()
elif num == 3:
    try:
        os.popen("cfdisk /dev/sda")
        os.popen("mkfs.fat -F 32 /dev/sda1")
        os.popen("mkfs.ext4 /dev/sda2")
        os.popen("mkswap /dev/sda3")
        os.popen("mount /dev/sda2 /mnt")
        os.popen("mkdir /mnt/boot")
        os.popen("mount /dev/sda1 /mnt/boot")
        os.popen("swapon /dev/sda3")
    except Exception as e:
        print("分区失败:"+e)
    finally:
        archinstall()
elif num == 4:
    try:
        os.popen("reflector -c China -a 6 --sort rate --save /etc/pacman.d/mirrorlist")
    except Exception as e:
        print("切换软件源失败:"+e)
    finally:
        archinstall()
elif num == 5:
    try:
        os.popen("pacstrap -K /mnt base linux linux-firmware")
        os.popen("pacman -S grub efibootmgr networkmanager plasma-meta konsole dolphin intel-ucode")
        os.popen("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
        os.popen("grub-mkconfig -o /boot/grub/grub.cfg")
    except Exception as e:
        print("安装系统失败:"+e)
    finally:
        archinstall()
elif num == 6:
    try:
        os.popen("genfstab -U /mnt >> /mnt/etc/fstab")
        os.popen("arch-chroot /mnt")
        os.popen("ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime")
        os.popen("hwclock --systohc")
        os.popen("sed -i s/#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g /etc/locale.gen")
        os.popen("sed -i s/#zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/g /etc/locale.gen")
        with open('/etc/locale.conf','a+',encoding='utf-8') as f:
            f.write('LANG=en_US.UTF-8')
        with open('/etc/hostname','a+',encoding='utf-8') as f:
            f.write('arch')
        with open('/etc/hosts','a+',encoding='utf-8') as f:
            f.write('127.0.0.1 localhost\n::1       localhost\n127.0.0.1 arch.localdomain arch')
        os.popen("systemctl enable sddm")
        os.popen("systemctl enable NetworkManager")
    except Exception as e:
        print("配置系统失败:"+e)
    finally:
        archinstall()
elif num == 6:
    try:
        os.popen("passwd")
        os.popen("useradd poo")
        os.popen("passwd poo")
    except Exception as e:
        print("创建用户失败:"+e)
    finally:
        archinstall()
else:
    print("选择错误")
    archinstall()