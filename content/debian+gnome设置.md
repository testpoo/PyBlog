title: debian+gnome设置
date: 2021-04-08
category: debian
tag: gnome

[TOC]

### 1. 安装软件

`sudo apt install intel-microcode fonts-noto-cjk arc-theme git ibus-rime rime-data-wubi`

### 2. 删除不需要软件

`apt autoremove --purge evolution libreoffice* gnome-calendar cheese gnome-chess gnome-clocks gnome-contacts evolution five-or-more four-in-a-row hitori gnome-klotski lightsoff gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles quadrapassel gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex gnome-todo totem gnome-2048 gnome-weather goldendict rhythmbox shotwell simple-scan synaptic termit transmission-gtk yelp zhcon aisleriot iagno gnome-sound-recorder fcitx5*`

### 3. 删除多余的扩展

- 删除/usr/share/gnome-shell/extensions下除user-theme以外的所有扩展