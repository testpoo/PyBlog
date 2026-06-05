title: virsh命令简述
date: 2026-06-05
category: 测试
tag: virsh, kvm

[TOC]

# 查看虚拟机状态：
virsh list --all

# 启动虚拟机 
virsh start debian 

# 关闭虚拟机：
virsh shutdown debian

# 强制停止虚拟机(断电）
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

# 创建快照
virsh snapshot-create-as debian debian_snap

# 删除快照
virsh snapshot-delete debian debian_snap

# 查看快照
virsh snapshot-list debian

# 恢复快照
virsh snapshot-revert debian debian_snap

# 查找上级快照
virsh snapshot-parent debian debian_snap