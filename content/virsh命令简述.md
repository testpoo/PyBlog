title: virsh命令简述
date: 2026-06-05
category: 测试
tag: virsh, kvm

[TOC]


### 1. 安装`kvm`
```
yum install -y qemu-kvm libvirt virt-install
```

### 2. 安装kvm虚拟机
```
virt-install \
--virt-type=kvm \
--name=ifcos1 \
--vcpus=2 \
--memory=8192 \
--cdrom=/home/iso/IFCOS3.1.1-x86_64-20180104162508.iso \
--disk path=/home/vms/ifcos1.qcow2,size=80,format=qcow2 \
--os-type=linux \
--graphics vnc,listen=0.0.0.0 \
--noautoconsole
#--extra-args='console=ttyS0'
```

### 3. 配置网桥连接模式
```
# 添加br0虚拟机网桥
brctl addbr br0

# 增加配置文件：/etc/sysconfig/network-scripts/ifcfg-br0
TYPE=Bridge
BOOTPROTO=static
NA_CONTROLLED=no
DEVICE=br0
ONBOOT=yes
IPADDR=192.168.211.50
NETMASK=255.255.255.0
GATEWAY=192.168.211.254
DNS1=218.30.19.40
DNS2=61.134.1.4

# 修改物理网卡配置：/etc/sysconfig/network-scripts/ifcfg-p4p1
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NM_CONTROLLED=no
NAME=p4p1
UUID=eb99acab-4332-4848-b031-3dcab72d3231
DEVICE=p4p1
ONBOOT=yes
BRIDGE=br0

# 在 /etc/libvirt/qemu/ifcos.xml修改网络配置
<interface type='bridge'>
      <mac address='52:54:00:e4:ec:55'/>
      <source bridge='br0'/>
      <model type='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
</interface>

# 应用配置
virsh define /etc/libvirt/qemu/ifcos.xml
```

### 4. 配置内存
```
virsh shutdown debian
virsh setmaxmem debian 15728640
virsh start debian
virsh setmem debian 10000000
virsh dominfo debian
```

### 5. 配置CPU
```
virsh setvcpus debian --maximum 4 --config
virsh vcpucount debian
virsh setvcpus debian --count 4 --config
```

### 6. 修改虚拟机名称
```
cd /etc/libvirt/qemu
virsh dumpxml ifcos58 > ifcos.xml
virsh snapshot-dumpxml ifcos58 ifcos_211.58 > ifcos_211.58.xml
virsh snapshot-dumpxml ifcos58 sicap_3.2.8base_40424 > sicap_3.2.8base_40424.xml
virsh snapshot-dumpxml ifcos58 sicap_3.3.1_200709 > sicap_3.3.1_200709.xml
mv /home/vms/ifcos58.qcow2 /home/vms/ifcos.qcow2
sed -i 's/ifcos58/ifcos/g' /etc/libvirt/qemu/ifcos.xml  /etc/libvirt/qemu/sicap_3.2.8base_40424.xml /etc/libvirt/qemu/sicap_3.3.1_200709.xml
virsh snapshot-delete ifcos58 sicap_3.3.1_200709
virsh undefine ifcos58
virsh define /etc/libvirt/qemu/ifcos.xml
virsh snapshot-create --redefine ifcos ifcos_211.58.xml
virsh snapshot-create --redefine ifcos sicap_3.2.8base_40424.xml
virsh snapshot-create --redefine ifcos sicap_3.3.1_200709.xml
```

### 7. 添加网卡
```
virsh domiflist ifcos
virsh attach-interface ifcos --type bridge --source br0
virsh dumpxml ifcos  >/etc/libvirt/qemu/ifcos.xml
virsh define /etc/libvirt/qemu/ifcos.xml
```

### 8. 删除virbr0虚拟网卡
```
#查看是否有连接相关虚拟设备
virsh net-list 
virsh net-destroy default 
virsh net-undefine default

#备份kvm虚拟机
qemu-img convert -c -O qcow2 centos7.qcow2 test.qcow2

#虚拟机添加磁盘
qemu-img create -f qcow2 kylin_sicap.qcow2 100G
virsh destroy kylin
virsh edit kylin
#修改磁盘配置，增加以下内容
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/home/vms/kylin_sicap.qcow2'/>
      <target dev='vdb' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x1'/>
    </disk>
virsh start kylin

#显示快照的继承关系
virsh snapshot-list ifcos --tree
```

### 9. 常用命令
```
# 查看虚拟机状态
virsh list --all

# 启动虚拟机
virsh start debian

# 关闭虚拟机
virsh shutdown debian

# 强制停止虚拟机(断电)
virsh destroy debian

# 删除虚拟机
virsh undefine debian

# 控制台连接虚拟机
virsh console debian

# 实时监控
virsh dominfo debian

# 动态扩容
virsh setvcpus debian 2 --live

# 内存热插拔
virsh setmem debian 2G --live

# 灾难恢复
virsh restore saved_state.file

# 性能分析
virsh domstats --cpu-total debian

# 创建内部快照
virsh snapshot-create-as debian debian_snap

# 删除内部快照
virsh snapshot-delete debian debian_snap

# 恢复内部快照
virsh snapshot-revert debian debian_snap

# 查看快照
virsh snapshot-list debian

# 查找上级快照
virsh snapshot-parent debian debian_snap
```

### 10. 创建外部快照

外部快照必须加上 --disk-only，只能保存磁盘状态
```
virsh snapshot-create-as --domain 虚拟机名 --name 快照名称 --disk-only --external
```
参数说明：
--disk-only：只做磁盘快照，不保存内存
--external：外部快照，生成独立差分 qcow2，原盘变为 backing 底层
--name snap_A：自定义快照名

指定快照文件存放路径（常用）
```
virsh snapshot-create-as \
--domain test-vm \
--name snap_A \
--disk-only \
--diskspec vda,snapshot=external,file=/var/lib/libvirt/images/test-vm-snapA.qcow2

virsh snapshot-create-as uos-server sicap260617 "安徽邮政升级包" --disk-only --atomic --diskspec vda,snapshot=external,file=/home/vms/uos-server.sicap260617
```
vda：虚拟机磁盘设备名
file=xxx：自定义快照差分文件路径

### 11. 创建差分盘

查看快照详细XML，拿到快照A磁盘文件路径
```
virsh snapshot-dumpxml 虚拟机名 --snapshotname 快照A名称
```
找到这一行，复制file=后的完整路径：
```
<source file="/xxx/xxx-snapA.qcow2"/>
```
以快照 A 为后端，新建空白差分盘
```
qemu-img create -f qcow2 -b /路径/快照A.qcow2 /路径/new-test.qcow2
```
然后将生成的差分盘路径写到source file中，如果不用了，删除这个差分盘。


### 12. 外部快照完整删除方案

```
# 关闭虚拟机
virsh destroy 虚拟机名
# 查看当前正在读写的 overlay 增量文件
virsh domblklist 虚拟机名
# 输出 vda        /xxx/vm-active.qcow2  这个就是存放你操作改动的文件

# 删除当前增量（所有操作全部丢弃）
rm -f /xxx/vm-active.qcow2

# 以快照 A 为底层，新建空白差分盘（回到纯净快照 A）
qemu-img create -f qcow2 -b /快照A完整路径 /xxx/vm-active.qcow2

# -b 父盘路径，-F 指定父盘格式（防报错）
qemu-img create -f qcow2 -b /home/vms/uos-server.uos_init_211.sicap241122 -F qcow2 /home/vms/uos-server.active

# 开机
virsh start 虚拟机名

# 配套清理 libvirt 快照列表
如果创建快照时带了--external元数据，列表里还残留 snapA 记录，只删元数据不删磁盘文件
virsh snapshot-delete 虚拟机名 --snapshotname snap_A --metadata

# 保留虚拟机所有数据，合并删除快照
```

### 13. 合并快照

如果你创建了链式快照 base ← snapA ← snapB ← active，想删掉中间snapA且保留全部数据，用blockcommit在线合并，无需关机。
示例：删除快照 A，把 A 的数据合并到底层 base

```
# 查看当前磁盘
virsh domblklist 虚拟机名
# 完整链查看
qemu-img info --backing-chain /当前active磁盘路径
```

#### 13.1 执行在线合并（vda 为磁盘设备）
```
virsh blockcommit 虚拟机名 vda \
--base=/base.qcow2 \
--top=/snapA.qcow2 \
--active --verbose --pivot

参数说明：
--base：底层镜像
--top：要删除的快照文件
--active --pivot：合并完成后自动切换磁盘指向，虚拟机不停机
```

合并完成确认虚拟机正常运行后，删除无用快照文件
```
rm -f /snapA.qcow2
```

清理 libvirt 快照元数据
```
virsh snapshot-delete 虚拟机名 --snapshotname snap_A --metadata
```

#### 13.2 关机离线合并（虚拟机停机更稳定）

```
# 关机
virsh destroy 虚拟机名
# 将snapA所有数据提交到底层base
qemu-img commit /snapA.qcow2
# 修改上层快照backing指向base，解除依赖
qemu-img rebase -u -b /base.qcow2 /snapB.qcow2
# 删除快照A文件
rm -f /snapA.qcow2
```