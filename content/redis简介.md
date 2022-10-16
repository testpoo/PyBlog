title: Redis入门教程
date: 2022-09-14
category: 笔记
tag: redis

[TOC]

# 1. Redis 简介

Redis 是完全开源的，遵守 BSD 协议，是一个高性能的 key-value 数据库。

Redis 与其他 key - value 缓存产品有以下三个特点：

- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
- Redis支持数据的备份，即master-slave模式的数据备份。

## 1.1 Redis 优势

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

## 1.2 Redis与其他key-value存储有什么不同？

- Redis有着更为复杂的数据结构并且提供对他们的原子性操作，这是一个不同于其他数据库的进化路径。Redis的数据类型都是基于基本数据结构的同时对程序员透明，无需进行额外的抽象。

- Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问。

# 2 Redis 安装

## 2.1 Linux下安装

**下载地址：** https://github.com/redis/redis/archive/7.0.4.tar.gz

登录linux后：

```
# 可能需要安装 apt install wget make gcc
mkdir redisfile
cd redisfile
wget https://github.com/redis/redis/archive/7.0.4.tar.gz
tar -zxvf 7.0.4.tar.gz
cd 7.0.4.tar.gz
make
cd src
```

打开文件夹，内容如下：

```
│  .gitattributes
│  .gitignore
│  00-RELEASENOTES
│  BUGS
│  CODE_OF_CONDUCT.md
│  CONTRIBUTING.md
│  COPYING
│  INSTALL
│  log
│  log1
│  Makefile
│  MANIFESTO
│  README.md
│  redis.conf
│  runtest
│  runtest-cluster
│  runtest-moduleapi
│  runtest-sentinel
│  SECURITY.md
│  sentinel.conf
│  TLS.md
├─.codespell
├─.github
├─deps
├─src
├─tests
└─utils
```

启动redis

`./redis-server`

```
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-server
8730:C 13 Sep 2022 09:18:28.712 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
8730:C 13 Sep 2022 09:18:28.712 # Redis version=7.0.4, bits=64, commit=00000000, modified=0, pid=8730, just started
8730:C 13 Sep 2022 09:18:28.712 # Warning: no config file specified, using the default config. In order to specify a config file use ./redis-server /path/to/redis.conf
8730:M 13 Sep 2022 09:18:28.713 * Increased maximum number of open files to 10032 (it was originally set to 1024).
8730:M 13 Sep 2022 09:18:28.713 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 7.0.4 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 8730
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

8730:M 13 Sep 2022 09:18:28.717 # Server initialized
8730:M 13 Sep 2022 09:18:28.717 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
8730:M 13 Sep 2022 09:18:28.718 * Ready to accept connections
```

启动 redis 服务进程后，使用测试客户端程序 redis-cli 和 redis 服务交互。 比如：

```
cd src
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-cli
127.0.0.1:6379> set foo bar
OK
127.0.0.1:6379> get foo
"bar"
127.0.0.1:6379>
```

其中127.0.0.1 是本机 IP ，6379 是 redis 服务端口。现在我们输入 PING 命令。

```
127.0.0.1:6379> ping
PONG
```

以上说明我们已经成功安装了redis。

**注：Redis 官方不建议在 windows 下使用 Redis，所以官网没有 windows 版本可以下载**。在这里不对win下的redis安装做讲解。

# 3. Redis 配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf。

你可以通过 **CONFIG** 命令查看或设置配置项。

### 3.1 语法

Redis CONFIG 命令格式如下：

`127.0.0.1:6379> config get config_setting_name`

### 3.2 实例

```
127.0.0.1:6379> config get loglevel
1) "loglevel"
2) "notice"
```

使用 ***** 号获取所有配置项：

### 3.3 实例

```
127.0.0.1:6379> config get *
  1) "cluster-require-full-coverage"
  2) "yes"
  3) "maxmemory-samples"
  4) "5"
  5) "oom-score-adj-values"
  6) "0 200 800"
  7) "slave-read-only"
  8) "yes"
  9) "slaveof"
 10) ""
 11) "stream-node-max-entries"
 12) "100"
 13) "repl-diskless-sync"
 14) "yes"
 15) "appendfilename"
 16) "appendonly.aof"
 17) "syslog-ident"
 18) "redis"
 19) "rdbchecksum"
 20) "yes"
 21) "sanitize-dump-payload"
 22) "no"
 23) "aof-disable-auto-gc"
 24) "no"
 25) "cluster-announce-ip"
 26) ""
 27) "replica-announce-port"
 28) "0"
 29) "min-slaves-max-lag"
 30) "10"
 31) "busy-reply-threshold"
 32) "5000"
 33) "ignore-warnings"
 34) ""
 35) "shutdown-timeout"
 36) "10"
 37) "bgsave_cpulist"
 38) ""
 39) "cluster-announce-tls-port"
 40) "0"
 41) "masterauth"
 42) ""
 43) "maxmemory-policy"
 44) "noeviction"
 45) "no-appendfsync-on-rewrite"
 46) "no"
 47) "appendonly"
 48) "no"
 49) "active-defrag-cycle-min"
 50) "1"
 51) "unixsocketperm"
 52) "0"
 53) "pidfile"
 54) ""
 55) "zset-max-listpack-value"
 56) "64"
 57) "cluster-config-file"
 58) "nodes.conf"
 59) "aof-use-rdb-preamble"
 60) "yes"
 61) "crash-log-enabled"
 62) "yes"
 63) "socket-mark-id"
 64) "0"
 65) "bio_cpulist"
 66) ""
 67) "masteruser"
 68) ""
 69) "replicaof"
 70) ""
 71) "dir"
 72) "/home/poo/redisfile/redis-7.0.4/src"
 73) "acl-pubsub-default"
 74) "resetchannels"
 75) "io-threads-do-reads"
 76) "no"
 77) "port"
 78) "6379"
 79) "set-proc-title"
 80) "yes"
 81) "proc-title-template"
 82) "{title} {listen-addr} {server-mode}"
 83) "min-replicas-max-lag"
 84) "10"
 85) "cluster-allow-replica-migration"
 86) "yes"
 87) "proto-max-bulk-len"
 88) "536870912"
 89) "replica-priority"
 90) "100"
 91) "cluster-replica-validity-factor"
 92) "10"
 93) "set-max-intset-entries"
 94) "512"
 95) "zset-max-ziplist-entries"
 96) "128"
 97) "lazyfree-lazy-expire"
 98) "no"
 99) "repl-disable-tcp-nodelay"
100) "no"
101) "requirepass"
102) ""
103) "cluster-announce-bus-port"
104) "0"
105) "slave-announce-ip"
106) ""
107) "server_cpulist"
108) ""
109) "oom-score-adj"
110) "no"
111) "replica-ignore-disk-write-errors"
112) "no"
113) "loglevel"
114) "notice"
115) "notify-keyspace-events"
116) ""
117) "lazyfree-lazy-user-del"
118) "no"
119) "lfu-log-factor"
120) "10"
121) "dbfilename"
122) "dump.rdb"
123) "slave-serve-stale-data"
124) "yes"
125) "bind-source-addr"
126) ""
127) "auto-aof-rewrite-min-size"
128) "67108864"
129) "cluster-port"
130) "0"
131) "slave-ignore-maxmemory"
132) "yes"
133) "logfile"
134) ""
135) "replica-lazy-flush"
136) "no"
137) "databases"
138) "16"
139) "replica-read-only"
140) "yes"
141) "slowlog-max-len"
142) "128"
143) "appendfsync"
144) "everysec"
145) "cluster-allow-pubsubshard-when-down"
146) "yes"
147) "hz"
148) "10"
149) "shutdown-on-sigint"
150) "default"
151) "maxclients"
152) "10000"
153) "client-output-buffer-limit"
154) "normal 0 0 0 slave 268435456 67108864 60 pubsub 33554432 8388608 60"
155) "rdb-del-sync-files"
156) "no"
157) "rdb-save-incremental-fsync"
158) "yes"
159) "slave-lazy-flush"
160) "no"
161) "activerehashing"
162) "yes"
163) "repl-diskless-sync-max-replicas"
164) "0"
165) "rdbcompression"
166) "yes"
167) "list-max-listpack-size"
168) "-2"
169) "cluster-slave-validity-factor"
170) "10"
171) "repl-backlog-size"
172) "1048576"
173) "slave-priority"
174) "100"
175) "hash-max-ziplist-entries"
176) "512"
177) "cluster-migration-barrier"
178) "1"
179) "stop-writes-on-bgsave-error"
180) "yes"
181) "latency-monitor-threshold"
182) "0"
183) "min-replicas-to-write"
184) "0"
185) "zset-max-ziplist-value"
186) "64"
187) "zset-max-listpack-entries"
188) "128"
189) "hash-max-listpack-entries"
190) "512"
191) "repl-timeout"
192) "60"
193) "save"
194) "3600 1 300 100 60 10000"
195) "maxmemory"
196) "0"
197) "shutdown-on-sigterm"
198) "default"
199) "repl-diskless-sync-delay"
200) "5"
201) "tracking-table-max-keys"
202) "1000000"
203) "enable-module-command"
204) "no"
205) "cluster-enabled"
206) "no"
207) "repl-ping-replica-period"
208) "10"
209) "syslog-enabled"
210) "no"
211) "list-compress-depth"
212) "0"
213) "appenddirname"
214) "appendonlydir"
215) "unixsocket"
216) ""
217) "aof-timestamp-enabled"
218) "no"
219) "enable-protected-configs"
220) "no"
221) "cluster-announce-port"
222) "0"
223) "cluster-replica-no-failover"
224) "no"
225) "lua-time-limit"
226) "5000"
227) "always-show-logo"
228) "no"
229) "bind"
230) "* -::*"
231) "supervised"
232) "no"
233) "replica-announce-ip"
234) ""
235) "cluster-slave-no-failover"
236) "no"
237) "lazyfree-lazy-eviction"
238) "no"
239) "active-expire-effort"
240) "1"
241) "io-threads"
242) "1"
243) "replica-serve-stale-data"
244) "yes"
245) "hll-sparse-max-bytes"
246) "3000"
247) "slave-announce-port"
248) "0"
249) "repl-ping-slave-period"
250) "10"
251) "activedefrag"
252) "no"
253) "stream-node-max-bytes"
254) "4096"
255) "jemalloc-bg-thread"
256) "yes"
257) "active-defrag-threshold-upper"
258) "100"
259) "hash-max-ziplist-value"
260) "64"
261) "client-query-buffer-limit"
262) "1073741824"
263) "maxmemory-eviction-tenacity"
264) "10"
265) "dynamic-hz"
266) "yes"
267) "enable-debug-command"
268) "no"
269) "propagation-error-behavior"
270) "ignore"
271) "disable-thp"
272) "yes"
273) "daemonize"
274) "no"
275) "auto-aof-rewrite-percentage"
276) "100"
277) "tcp-backlog"
278) "511"
279) "crash-memcheck-enabled"
280) "yes"
281) "replica-announced"
282) "yes"
283) "aof-rewrite-incremental-fsync"
284) "yes"
285) "aof-load-truncated"
286) "yes"
287) "aof_rewrite_cpulist"
288) ""
289) "latency-tracking"
290) "yes"
291) "cluster-announce-hostname"
292) ""
293) "syslog-facility"
294) "local0"
295) "lfu-decay-time"
296) "1"
297) "replica-ignore-maxmemory"
298) "yes"
299) "slowlog-log-slower-than"
300) "10000"
301) "active-defrag-threshold-lower"
302) "10"
303) "maxmemory-clients"
304) "0"
305) "min-slaves-to-write"
306) "0"
307) "acllog-max-len"
308) "128"
309) "repl-diskless-load"
310) "disabled"
311) "hash-max-listpack-value"
312) "64"
313) "active-defrag-ignore-bytes"
314) "104857600"
315) "latency-tracking-info-percentiles"
316) "50 99 99.9"
317) "tcp-keepalive"
318) "300"
319) "protected-mode"
320) "yes"
321) "timeout"
322) "0"
323) "list-max-ziplist-size"
324) "-2"
325) "cluster-link-sendbuf-limit"
326) "0"
327) "aclfile"
328) ""
329) "cluster-preferred-endpoint-type"
330) "ip"
331) "active-defrag-cycle-max"
332) "25"
333) "lazyfree-lazy-server-del"
334) "no"
335) "cluster-allow-reads-when-down"
336) "no"
337) "active-defrag-max-scan-fields"
338) "1000"
339) "cluster-node-timeout"
340) "15000"
341) "lazyfree-lazy-user-flush"
342) "no"
343) "repl-backlog-ttl"
344) "3600"
```

## 3.4 编辑配置

你可以通过修改 redis.conf 文件或使用 **CONFIG set** 命令来修改配置。

### 3.4.1 语法

**CONFIG SET** 命令基本语法：

`redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE`

### 3.4.2 实例

```
# loglevel只能是以下四个之一：debug, verbose, notice, warning
127.0.0.1:6379> config get loglevel
1) "loglevel"
2) "notice"
127.0.0.1:6379> config set loglevel "test"
(error) ERR CONFIG SET failed (possibly related to argument 'loglevel') - argument(s) must be one of the following: debug, verbose, notice, warning
127.0.0.1:6379> config set loglevel "warning"
OK
127.0.0.1:6379> config get loglevel
1) "loglevel"
2) "warning"
```

## 3.5 参数说明

redis.conf 配置项说明如下：

| 序号  | 配置项                                                                                                                                                                                           | 说明                                                                                                                                                                           |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `daemonize no`                                                                                                                                                                                | Redis 默认不是以守护进程的方式运行，可以通过该配置项修改，使用 yes 启用守护进程                                                                                                                                |
| 2   | `pidfile /var/run/redis.pid`                                                                                                                                                                  | 当 Redis 以守护进程方式运行时，Redis 默认会把 pid 写入 /var/run/redis.pid 文件，可以通过 pidfile 指定                                                                                                   |
| 3   | `port 6379`                                                                                                                                                                                   | 指定 Redis 监听端口，默认端口为 6379                                                                                                                                                     |
| 4   | `bind 127.0.0.1`                                                                                                                                                                              | 绑定的主机地址                                                                                                                                                                      |
| 5   | `timeout 300`                                                                                                                                                                                 | 当客户端闲置多长秒后关闭连接，如果指定为 0 ，表示关闭该功能                                                                                                                                              |
| 6   | `loglevel notice`                                                                                                                                                                             | 指定日志记录级别，Redis 总共支持四个级别：debug、verbose、notice、warning，默认为 notice                                                                                                              |
| 7   | `logfile stdout`                                                                                                                                                                              | 日志记录方式，默认为标准输出，如果配置 Redis 为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给 /dev/null                                                                                                    |
| 8   | `databases 16`                                                                                                                                                                                | 设置数据库的数量，默认数据库为0，可以使用SELECT 命令在连接上指定数据库id                                                                                                                                    |
| 9   | `save <seconds> <changes>`<br />Redis 默认配置文件中提供了三个条件：<br />**save 900 1**<br />**save 300 10**<br />**save 60 10000**<br />分别表示 900 秒（15 分钟）内有 1 个更改，300 秒（5 分钟）内有 10 个更改以及 60 秒内有 10000 个更改。 | 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合                                                                                                                                       |
| 10  | `rdbcompression yes`                                                                                                                                                                          | 指定存储至本地数据库时是否压缩数据，默认为 yes，Redis 采用 LZF 压缩，如果为了节省 CPU 时间，可以关闭该选项，但会导致数据库文件变的巨大                                                                                                |
| 11  | `dbfilename dump.rdb`                                                                                                                                                                         | 指定本地数据库文件名，默认值为 dump.rdb                                                                                                                                                     |
| 12  | `dir ./`                                                                                                                                                                                      | 指定本地数据库存放目录                                                                                                                                                                  |
| 13  | `slaveof <masterip> <masterport>`                                                                                                                                                             | 设置当本机为 slave 服务时，设置 master 服务的 IP 地址及端口，在 Redis 启动时，它会自动从 master 进行数据同步                                                                                                      |
| 14  | `masterauth <master-password>`                                                                                                                                                                | 当 master 服务设置了密码保护时，slave 服务连接 master 的密码                                                                                                                                    |
| 15  | `requirepass foobared`                                                                                                                                                                        | 设置 Redis 连接密码，如果配置了连接密码，客户端在连接 Redis 时需要通过 AUTH <password> 命令提供密码，默认关闭                                                                                                       |
| 16  | `maxclients 128`                                                                                                                                                                              | 设置同一时间最大客户端连接数，默认无限制，Redis 可以同时打开的客户端连接数为 Redis 进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis 会关闭新的连接并向客户端返回 max number of clients reached 错误信息                |
| 17  | `maxmemory <bytes>`                                                                                                                                                                           | 指定 Redis 最大内存限制，Redis 在启动时会把数据加载到内存中，达到最大内存后，Redis 会先尝试清除已到期或即将到期的 Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis 新的 vm 机制，会把 Key 存放内存，Value 会存放在 swap 区               |
| 18  | `appendonly no`                                                                                                                                                                               | 指定是否在每次更新操作后进行日志记录，Redis 在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis 本身同步数据文件是按上面 save 条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为 no                                           |
| 19  | `appendfilename appendonly.aof`                                                                                                                                                               | 指定更新日志文件名，默认为 appendonly.aof                                                                                                                                                 |
| 20  | `appendfsync everysec`                                                                                                                                                                        | 指定更新日志条件，共有 3 个可选值：<br><br>- **no**：表示等操作系统进行数据缓存同步到磁盘（快）<br>- **always**：表示每次更新操作后手动调用 fsync() 将数据写到磁盘（慢，安全）<br>- **everysec**：表示每秒同步一次（折中，默认值）                             |
| 21  | `vm-enabled no`                                                                                                                                                                               | 指定是否启用虚拟内存机制，默认值为 no，简单的介绍一下，VM 机制将数据分页存放，由 Redis 将访问量较少的页即冷数据 swap 到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析 Redis 的 VM 机制）                                                       |
| 22  | `vm-swap-file /tmp/redis.swap`                                                                                                                                                                | 虚拟内存文件路径，默认值为 /tmp/redis.swap，不可多个 Redis 实例共享                                                                                                                                |
| 23  | `vm-max-memory 0`                                                                                                                                                                             | 将所有大于 vm-max-memory 的数据存入虚拟内存，无论 vm-max-memory 设置多小，所有索引数据都是内存存储的(Redis 的索引数据 就是 keys)，也就是说，当 vm-max-memory 设置为 0 的时候，其实是所有 value 都存在于磁盘。默认值为 0                              |
| 24  | `vm-page-size 32`                                                                                                                                                                             | Redis swap 文件分成了很多的 page，一个对象可以保存在多个 page 上面，但一个 page 上不能被多个对象共享，vm-page-size 是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page 大小最好设置为 32 或者 64bytes；如果存储很大大对象，则可以使用更大的 page，如果不确定，就使用默认值 |
| 25  | `vm-pages 134217728`                                                                                                                                                                          | 设置 swap 文件中的 page 数量，由于页表（一种表示页面空闲或使用的 bitmap）是在放在内存中的，，在磁盘上每 8 个 pages 将消耗 1byte 的内存。                                                                                       |
| 26  | `vm-max-threads 4`                                                                                                                                                                            | 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟。默认值为4                                                                                                    |
| 27  | `glueoutputbuf yes`                                                                                                                                                                           | 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启                                                                                                                                             |
| 28  | `hash-max-zipmap-entries 64`<br>`hash-max-zipmap-value 512`                                                                                                                                   | 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法                                                                                                                                        |
| 29  | `activerehashing yes`                                                                                                                                                                         | 指定是否激活重置哈希，默认为开启（后面在介绍 Redis 的哈希算法时具体介绍）                                                                                                                                     |
| 30  | `include /path/to/local.conf`                                                                                                                                                                 | 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件                                                                                                                 |

# 4. Redis 数据类型

Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

## 4.1 String（字符串）

string 是 redis 最基本的类型，一个 key 对应一个 value。

string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。

string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

### 4.1.1 实例

```
127.0.0.1:6379> set test "suninfo"
OK
127.0.0.1:6379> get test
"suninfo"
```

在以上实例中我们使用了 Redis 的 **SET** 和 **GET** 命令。键为 test，对应的值为 **suninfo**。

**注意：** 一个键最大能存储 512MB。

## 4.2 Hash（哈希）

Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。

### 4.2.1 实例

del test 用于删除前面测试用过的 key，不然会报错：**(error) WRONGTYPE Operation against a key holding the wrong kind of value**

```
127.0.0.1:6379> set test "suninfo"
OK
127.0.0.1:6379> get test
"suninfo"
127.0.0.1:6379> hmset test field1 "sun" field2 "info"
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> del test
(integer) 1
127.0.0.1:6379> hmset test field1 "sun" field2 "info"
OK
127.0.0.1:6379> hget test field1
"sun"
127.0.0.1:6379> hget test field2
"info"
```

实例中我们使用了 Redis **HMSET, HGET** 命令，**HMSET** 设置了两个 field=>value 对, HGET 获取对应 **field** 对应的 **value**。

每个 hash 可以存储 232 -1 键值对（40多亿）。

## 4.3 List（列表）

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

### 4.3.1 实例

```
127.0.0.1:6379> del test
(integer) 1
127.0.0.1:6379> lpush test redis
(integer) 1
127.0.0.1:6379> lpush test mongodb
(integer) 2
127.0.0.1:6379> lpush test rabbitmq
(integer) 3
127.0.0.1:6379> lrange test 0 10
1) "rabbitmq"
2) "mongodb"
3) "redis"
127.0.0.1:6379> rpush test mysql
(integer) 4
127.0.0.1:6379> lrange test 0 10
1) "rabbitmq"
2) "mongodb"
3) "redis"
4) "mysql"
```

列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。

## 4.4 Set（集合）

Redis 的 Set 是 string 类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

### 4.4.1 sadd 命令

添加一个 string 元素到 key 对应的 set 集合中，成功返回 1，如果元素已经在集合中返回 0。

`sadd key member`

### 4.4.2 实例

```
127.0.0.1:6379> del test
(integer) 1
127.0.0.1:6379> sadd test redis
(integer) 1
127.0.0.1:6379> sadd test mongodb
(integer) 1
127.0.0.1:6379> sadd test rabbitmq
(integer) 1
127.0.0.1:6379> sadd test rabbitmq
(integer) 0
127.0.0.1:6379> smembers test
1) "mongodb"
2) "rabbitmq"
3) "redis"
```

**注意：** 以上实例中 rabbitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1(4294967295, 每个集合可存储40多亿个成员)。

## 4.5 zset(sorted set：有序集合)

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。

### 4.5.1 zadd 命令

添加元素到集合，元素在集合中存在则更新对应score

`zadd key score member`

### 4.5.2 实例

```
127.0.0.1:6379> del test
(integer) 1
127.0.0.1:6379> zadd test 0 redis
(integer) 1
127.0.0.1:6379> zadd test 0 mongodb
(integer) 1
127.0.0.1:6379> zadd test 0 rabbitmq
(integer) 1
127.0.0.1:6379> zadd test 0 rabbitmq
(integer) 0
127.0.0.1:6379> zrangebyscore test 0 1000
1) "mongodb"
2) "rabbitmq"
3) "redis"
```

# 5 Redis 命令

Redis 命令用于在 redis 服务上执行操作。

要在 redis 服务上执行命令需要一个 redis 客户端。Redis 客户端在我们之前下载的的 redis 的安装包中。

## 5.1 在本机上执行命令

### 5.1.1 语法

Redis 客户端的基本语法为：

`$ redis-cli`

### 5.1.2 实例

以下实例讲解了如何启动 redis 客户端：

启动 redis 服务器，打开终端并输入命令 **redis-cli**，该命令会连接本地的 redis 服务。

```
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-cli
127.0.0.1:6379> ping
PONG
```

在以上实例中我们连接到本地的 redis 服务并执行 **PING** 命令，该命令用于检测 redis 服务是否启动。

## 5.2 在远程服务上执行命令

如果需要在远程 redis 服务上执行命令，同样我们使用的也是 **redis-cli** 命令。

### 5.2.1 语法

`$ redis-cli -h host -p port -a password`

### 5.2.2 实例

以下实例演示了如何连接到主机为 127.0.0.1，端口为 6379 ，密码为 123456的 redis 服务上。

```
# 因为redis没有设置密码，先给设置一个用于演示
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-cli
127.0.0.1:6379> config set requirepass 123456
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "123456"
127.0.0.1:6379> exit
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-cli -h 127.0.0.1 -p 6379 -a "123456"
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
127.0.0.1:6379> ping
PONG
```

# 6. Redis 键(key)

## 6.1 Redis 键(key)

Redis 键命令用于管理 redis 的键。

### 6.1.1 语法

Redis 键命令的基本语法如下：

`127.0.0.1:6379> COMMAND KEY_NAME`

### 6.1.2 实例

```
127.0.0.1:6379> set testkey redis
OK
127.0.0.1:6379> del testkey
(integer) 1
```

在以上实例中 **DEL** 是一个命令， **testkey** 是一个键。 如果键被删除成功，命令执行后输出 **(integer) 1**，否则将输出 **(integer) 0**

## 6.2 Redis keys 命令

下表给出了与 Redis 键相关的基本命令：

| 序号  | 命令及描述                                                                                                                 |
| --- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | DEL key<br>该命令用于在 key 存在时删除 key。                                                                                      |
| 2   | DUMP key<br>序列化给定 key ，并返回被序列化的值。                                                                                     |
| 3   | EXISTS key<br>检查给定 key 是否存在。                                                                                          |
| 4   | EXPIRE key seconds<br>为给定 key 设置过期时间，以秒计。                                                                             |
| 5   | EXPIREAT key timestamp<br>EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。 不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp)。 |
| 6   | PEXPIRE key milliseconds<br>设置 key 的过期时间以毫秒计。                                                                         |
| 7   | PEXPIREAT key milliseconds-timestamp<br>设置 key 过期时间的时间戳(unix timestamp) 以毫秒计                                          |
| 8   | KEYS pattern<br>查找所有符合给定模式( pattern)的 key 。                                                                           |
| 9   | MOVE key db<br>将当前数据库的 key 移动到给定的数据库 db 当中。                                                                           |
| 10  | PERSIST key<br>移除 key 的过期时间，key 将持久保持。                                                                                |
| 11  | PTTL key<br>以毫秒为单位返回 key 的剩余的过期时间。                                                                                    |
| 12  | TTL key<br>以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。                                                                 |
| 13  | RANDOMKEY<br>从当前数据库中随机返回一个 key 。                                                                                      |
| 14  | RENAME key newkey<br>修改 key 的名称                                                                                       |
| 15  | RENAMENX key newkey<br>仅当 newkey 不存在时，将 key 改名为 newkey 。                                                              |
| 16  | SCAN cursor [MATCH pattern] [COUNT count]<br>迭代数据库中的数据库键。                                                             |
| 17  | TYPE key<br>返回 key 所储存的值的类型。                                                                                          |

更多命令请参考：https://redis.io/commands

# 7. Redis 字符串(String)

Redis 字符串数据类型的相关命令用于管理 redis 字符串值，基本语法如下：

## 7.1 Redis 字符串(String)

### 7.1.1 语法

`127.0.0.1:6379> COMMAND KEY_NAME`

### 7.1.2 实例

```
127.0.0.1:6379> set testkey redis
OK
127.0.0.1:6379> get testkey
"redis"
```

在以上实例中我们使用了 **SET** 和 **GET** 命令，键为 **testkey**。

## 7.2 Redis 字符串命令

下表列出了常用的 redis 字符串命令：

| 序号  | 命令及描述                                                                                         |
| --- | --------------------------------------------------------------------------------------------- |
| 1   | SET key value<br>设置指定 key 的值。                                                                 |
| 2   | GET key<br>获取指定 key 的值。                                                                       |
| 3   | GETRANGE key start end<br>返回 key 中字符串值的子字符                                                    |
| 4   | GETSET key value<br>将给定 key 的值设为 value ，并返回 key 的旧值(old value)。                               |
| 5   | GETBIT key offset<br>对 key 所储存的字符串值，获取指定偏移量上的位(bit)。                                          |
| 6   | MGET key1 [key2..]<br>获取所有(一个或多个)给定 key 的值。                                                   |
| 7   | SETBIT key offset value<br>对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)。                                 |
| 8   | SETEX key seconds value<br>将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以秒为单位)。                  |
| 9   | SETNX key value<br>只有在 key 不存在时设置 key 的值。                                                     |
| 10  | SETRANGE key offset value<br>用 value 参数覆写给定 key 所储存的字符串值，从偏移量 offset 开始。                      |
| 11  | STRLEN key<br>返回 key 所储存的字符串值的长度。                                                             |
| 12  | MSET key value [key value ...]<br>同时设置一个或多个 key-value 对。                                      |
| 13  | MSETNX key value [key value ...]<br>同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。                  |
| 14  | PSETEX key milliseconds value<br>这个命令和 SETEX 命令相似，但它以毫秒为单位设置 key 的生存时间，而不是像 SETEX 命令那样，以秒为单位。 |
| 15  | INCR key<br>将 key 中储存的数字值增一。                                                                  |
| 16  | INCRBY key increment<br>将 key 所储存的值加上给定的增量值（increment） 。                                      |
| 17  | INCRBYFLOAT key increment<br>将 key 所储存的值加上给定的浮点增量值（increment） 。                               |
| 18  | DECR key<br>将 key 中储存的数字值减一。                                                                  |
| 19  | DECRBY key decrement<br>key 所储存的值减去给定的减量值（decrement） 。                                        |
| 20  | APPEND key value<br>如果 key 已经存在并且是一个字符串， APPEND 命令将指定的 value 追加到该 key 原来值（value）的末尾。          |

更多命令请参考：https://redis.io/commands

# 8. Redis 哈希(Hash)

## 8.1 Redis 哈希(Hash)

Redis hash 是一个 string 类型的 field（字段） 和 value（值） 的映射表，hash 特别适合用于存储对象。

Redis 中每个 hash 可以存储 2<sup>32</sup> - 1 键值对（40多亿）。

### 8.1.1 实例

```
127.0.0.1:6379> hmset testkey name "redis tutorial" description "redis basic commands for caching" number 200 allno 30000
OK
127.0.0.1:6379> hgetall testkey
 1) "name"
 2) "redis tutorial"
 3) "description"
 4) "redis basic commands for caching"
 5) "likes"
 6) "20"
 7) "visitors"
 8) "23000"
 9) "number"
10) "200"
11) "allno"
12) "30000"
```

在以上实例中，我们设置了 redis 的一些描述信息(name, description, number, allno) 到哈希表的 **testkey** 中。

## 8.2 Redis hash 命令

下表列出了 redis hash 基本的相关命令：

| 序号  | 命令及描述                                                                             |
| --- | --------------------------------------------------------------------------------- |
| 1   | HDEL key field1 [field2]<br>删除一个或多个哈希表字段                                          |
| 2   | HEXISTS key field<br>查看哈希表 key 中，指定的字段是否存在。                                       |
| 3   | HGET key field<br>获取存储在哈希表中指定字段的值。                                                |
| 4   | HGETALL key<br>获取在哈希表中指定 key 的所有字段和值                                              |
| 5   | HINCRBY key field increment<br>为哈希表 key 中的指定字段的整数值加上增量 increment 。                |
| 6   | HINCRBYFLOAT key field increment<br>为哈希表 key 中的指定字段的浮点数值加上增量 increment 。          |
| 7   | HKEYS key<br>获取所有哈希表中的字段                                                          |
| 8   | HLEN key<br>获取哈希表中字段的数量                                                           |
| 9   | HMGET key field1 [field2]<br>获取所有给定字段的值                                           |
| 10  | HMSET key field1 value1 [field2 value2 ]<br>同时将多个 field-value (域-值)对设置到哈希表 key 中。 |
| 11  | HSET key field value<br>将哈希表 key 中的字段 field 的值设为 value 。                          |
| 12  | HSETNX key field value<br>只有在字段 field 不存在时，设置哈希表字段的值。                             |
| 13  | HVALS key<br>获取哈希表中所有值。                                                           |
| 14  | HSCAN key cursor [MATCH pattern] [COUNT count]<br>迭代哈希表中的键值对。                     |

更多命令请参考：https://redis.io/commands

# 9. Redis 列表(List)

## 9.1 Redis 列表(List)

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

一个列表最多可以包含 232 - 1 个元素 (4294967295, 每个列表超过40亿个元素)。

### 9.1.1 实例

```
127.0.0.1:6379> del testkey
(integer) 1
127.0.0.1:6379> lpush testkey redis
(integer) 1
127.0.0.1:6379> lpush mongodb
(error) ERR wrong number of arguments for 'lpush' command
127.0.0.1:6379> lpush testkey mongodb
(integer) 2
127.0.0.1:6379> lpush testkey mysql
(integer) 3
127.0.0.1:6379> lrange testkey 0 10
1) "mysql"
2) "mongodb"
3) "redis"
```

在以上实例中我们使用了 **LPUSH** 将三个值插入了名为 **testkey** 的列表当中。

## 9.2 Redis 列表命令

下表列出了列表相关的基本命令：

| 序号  | 命令及描述                                                                                                   |
| --- | ------------------------------------------------------------------------------------------------------- |
| 1   | BLPOP key1 [key2 ] timeout<br>移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。                             |
| 2   | BRPOP key1 [key2 ] timeout<br>移出并获取列表的最后一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。                            |
| 3   | BRPOPLPUSH source destination timeout<br>从列表中弹出一个值，将弹出的元素插入到另外一个列表中并返回它； 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。 |
| 4   | LINDEX key index<br>通过索引获取列表中的元素                                                                        |
| 5   | LINSERT key BEFORE\|AFTER pivot value<br>在列表的元素前或者后插入元素                                                 |
| 6   | LLEN key<br>获取列表长度                                                                                      |
| 7   | LPOP key<br>移出并获取列表的第一个元素                                                                               |
| 8   | LPUSH key value1 [value2]<br>将一个或多个值插入到列表头部                                                             |
| 9   | LPUSHX key value<br>将一个值插入到已存在的列表头部                                                                     |
| 10  | LRANGE key start stop<br>获取列表指定范围内的元素                                                                   |
| 11  | LREM key count value<br>移除列表元素                                                                          |
| 12  | LSET key index value<br>通过索引设置列表元素的值                                                                    |
| 13  | LTRIM key start stop<br>对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。                            |
| 14  | RPOP key<br>移除列表的最后一个元素，返回值为移除的元素。                                                                      |
| 15  | RPOPLPUSH source destination<br>移除列表的最后一个元素，并将该元素添加到另一个列表并返回                                            |
| 16  | RPUSH key value1 [value2]<br>在列表中添加一个或多个值                                                               |
| 17  | RPUSHX key value<br>为已存在的列表添加值                                                                          |

# 10. Redis 集合(Set)

## 10.1 Redis 集合(Set)

Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

集合对象的编码可以是 intset 或者 hashtable。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

### 10.1.1 实例

```
127.0.0.1:6379> del testkey
(integer) 1
127.0.0.1:6379> sadd testkey redis
(integer) 1
127.0.0.1:6379> sadd testkey mongodb
(integer) 1
127.0.0.1:6379> sadd testkey mysql
(integer) 1
127.0.0.1:6379> sadd testkey mysql
(integer) 0
127.0.0.1:6379> smembers testkey
1) "mongodb"
2) "mysql"
3) "redis"
```

在以上实例中我们通过 **SADD** 命令向名为 **testkey** 的集合插入的三个元素。

## 10.2 Redis 集合命令

下表列出了 Redis 集合基本命令：

| 序号  | 命令及描述                                                                       |
| --- | --------------------------------------------------------------------------- |
| 1   | SADD key member1 [member2]<br>向集合添加一个或多个成员                                  |
| 2   | SCARD key<br>获取集合的成员数                                                       |
| 3   | SDIFF key1 [key2]<br>返回第一个集合与其他集合之间的差异。                                     |
| 4   | SDIFFSTORE destination key1 [key2]<br>返回给定所有集合的差集并存储在 destination 中         |
| 5   | SINTER key1 [key2]<br>返回给定所有集合的交集                                           |
| 6   | SINTERSTORE destination key1 [key2]<br>返回给定所有集合的交集并存储在 destination 中        |
| 7   | SISMEMBER key member<br>判断 member 元素是否是集合 key 的成员                           |
| 8   | SMEMBERS key<br>返回集合中的所有成员                                                  |
| 9   | SMOVE source destination member<br>将 member 元素从 source 集合移动到 destination 集合 |
| 10  | SPOP key<br>移除并返回集合中的一个随机元素                                                 |
| 11  | SRANDMEMBER key [count]<br>返回集合中一个或多个随机数                                    |
| 12  | SREM key member1 [member2]<br>移除集合中一个或多个成员                                  |
| 13  | SUNION key1 [key2]<br>返回所有给定集合的并集                                           |
| 14  | SUNIONSTORE destination key1 [key2]<br>所有给定集合的并集存储在 destination 集合中         |
| 15  | SSCAN key cursor [MATCH pattern] [COUNT count]<br>迭代集合中的元素                  |

# 11. Redis 有序集合(sorted set)

## 11.1 Redis 有序集合(sorted set)

Redis 有序集合和集合一样也是 string 类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个 double 类型的分数。redis 正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数(score)却可以重复。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。 集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

### 11.1.1 实例

```
127.0.0.1:6379> del testkey
(integer) 1
127.0.0.1:6379> zadd testkey 1 redis
(integer) 1
127.0.0.1:6379> zadd testkey 2 mongodb
(integer) 1
127.0.0.1:6379> zadd testkey 3 mysql
(integer) 1
127.0.0.1:6379> zadd testkey 1 mysql
(integer) 0
127.0.0.1:6379> zadd testkey 4 mysql
(integer) 0
127.0.0.1:6379> zrange testkey 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "mysql"
6) "4"
```

在以上实例中我们通过命令 **ZADD** 向 redis 的有序集合中添加了三个值并关联上分数。

## 11.2 Redis 有序集合命令

下表列出了 redis 有序集合的基本命令:

| 序号  | 命令及描述                                                                                         |
| --- | --------------------------------------------------------------------------------------------- |
| 1   | ZADD key score1 member1 [score2 member2]<br>向有序集合添加一个或多个成员，或者更新已存在成员的分数                       |
| 2   | ZCARD key<br>获取有序集合的成员数                                                                       |
| 3   | ZCOUNT key min max<br>计算在有序集合中指定区间分数的成员数                                                      |
| 4   | ZINCRBY key increment member<br>有序集合中对指定成员的分数加上增量 increment                                   |
| 5   | ZINTERSTORE destination numkeys key [key ...]<br>计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 destination 中 |
| 6   | ZLEXCOUNT key min max<br>在有序集合中计算指定字典区间内成员数量                                                  |
| 7   | ZRANGE key start stop [WITHSCORES]<br>通过索引区间返回有序集合指定区间内的成员                                    |
| 8   | ZRANGEBYLEX key min max [LIMIT offset count]<br>通过字典区间返回有序集合的成员                               |
| 9   | ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT]<br>通过分数返回有序集合指定区间内的成员                          |
| 10  | ZRANK key member<br>返回有序集合中指定成员的索引                                                            |
| 11  | ZREM key member [member ...]<br>移除有序集合中的一个或多个成员                                               |
| 12  | ZREMRANGEBYLEX key min max<br>移除有序集合中给定的字典区间的所有成员                                             |
| 13  | ZREMRANGEBYRANK key start stop<br>移除有序集合中给定的排名区间的所有成员                                         |
| 14  | ZREMRANGEBYSCORE key min max<br>移除有序集合中给定的分数区间的所有成员                                           |
| 15  | ZREVRANGE key start stop [WITHSCORES]<br>返回有序集中指定区间内的成员，通过索引，分数从高到低                           |
| 16  | ZREVRANGEBYSCORE key max min [WITHSCORES]<br>返回有序集中指定分数区间内的成员，分数从高到低排序                        |
| 17  | ZREVRANK key member<br>返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序                                     |
| 18  | ZSCORE key member<br>返回有序集中，成员的分数值                                                            |
| 19  | ZUNIONSTORE destination numkeys key [key ...]<br>计算给定的一个或多个有序集的并集，并存储在新的 key 中                |
| 20  | ZSCAN key cursor [MATCH pattern] [COUNT count]<br>迭代有序集合中的元素（包括元素成员和元素分值）                     |

# 12. Redis HyperLogLog

Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定的、并且是很小的。

在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2<sup>64</sup> 个不同元素的基数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。

但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

## 12.1 什么是基数?

比如数据集 {1, 3, 5, 7, 5, 7, 8}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8}, 基数(不重复元素)为5。 基数估计就是在误差可接受的范围内，快速计算基数。

## 12.2 实例

以下实例演示了 HyperLogLog 的工作过程：

```
127.0.0.1:6379> del testkey
(integer) 1
127.0.0.1:6379> pfadd testkey "redis"
(integer) 1
127.0.0.1:6379> pfadd testkey "mongodb"
(integer) 1
127.0.0.1:6379> pfadd testkey "mysql"
(integer) 1
127.0.0.1:6379> pfcount testkey
(integer) 3
```

## 12.3 Redis HyperLogLog 命令

下表列出了 redis HyperLogLog 的基本命令：

| 序号  | 命令及描述                                                                          |
| --- | ------------------------------------------------------------------------------ |
| 1   | PFADD key element [element ...]<br>添加指定元素到 HyperLogLog 中。                      |
| 2   | PFCOUNT key [key ...]<br>返回给定 HyperLogLog 的基数估算值。                              |
| 3   | PFMERGE destkey sourcekey [sourcekey ...]<br>将多个 HyperLogLog 合并为一个 HyperLogLog |

# 13. Redis 发布订阅

Redis 发布订阅 (pub/sub) 是一种消息通信模式：发送者 (pub) 发送消息，订阅者 (sub) 接收消息。

Redis 客户端可以订阅任意数量的频道。

下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：

![](https://www.runoob.com/wp-content/uploads/2014/11/pubsub1.png)

当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：

![](https://www.runoob.com/wp-content/uploads/2014/11/pubsub2.png)

## 13.1 实例

以下实例演示了发布订阅是如何工作的，需要开启两个 redis-cli 客户端。

在我们实例中我们创建了订阅频道名为 **testChat**:

## 13.2 第一个 redis-cli 客户端

```
127.0.0.1:6379> subscribe testChat
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "testChat"
3) (integer) 1
```

现在，我们先重新开启个 redis 客户端，然后在同一个频道 testChat 发布两次消息，订阅者就能接收到消息。

## 13.3 第二个 redis-cli 客户端

```
127.0.0.1:6379> publish testChat "Redis publish test"
(integer) 1
127.0.0.1:6379> publish testChat "Learn redis by poo"
(integer) 1
```

## 13.4 订阅者的客户端会显示如下消息

```
127.0.0.1:6379> subscribe testChat
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "testChat"
3) (integer) 1
1) "message"
2) "testChat"
3) "Redis publish test"
1) "message"
2) "testChat"
3) "Learn redis by poo"
```

## 13.5 Redis 发布订阅命令

下表列出了 redis 发布订阅常用命令：

| 序号  | 命令及描述                                                       |
| --- | ----------------------------------------------------------- |
| 1   | PSUBSCRIBE pattern [pattern ...]<br>订阅一个或多个符合给定模式的频道。       |
| 2   | PUBSUB subcommand [argument [argument ...]]<br>查看订阅与发布系统状态。 |
| 3   | PUBLISH channel message<br>将信息发送到指定的频道。                     |
| 4   | PUNSUBSCRIBE [pattern [pattern ...]]<br>退订所有给定模式的频道。        |
| 5   | SUBSCRIBE channel [channel ...]<br>订阅给定的一个或多个频道的信息。         |
| 6   | UNSUBSCRIBE [channel [channel ...]]<br>指退订给定的频道。            |

# 14. Redis 事务

Redis 事务可以一次执行多个命令， 并且带有以下三个重要的保证：

- 批量操作在发送 EXEC 命令前被放入队列缓存。
- 收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
- 在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。

一个事务从开始到执行会经历以下三个阶段：

- 开始事务。
- 命令入队。
- 执行事务。

## 14.1 实例

以下是一个事务的例子， 它先以 **MULTI** 开始一个事务， 然后将多个命令入队到事务中， 最后由 **EXEC** 命令触发事务， 一并执行事务中的所有命令：

```
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> set book-name "Mastering C++ in 21 days"
QUEUED
127.0.0.1:6379(TX)> get book-name
QUEUED
127.0.0.1:6379(TX)> sadd tag "C++ Programming" "Mastering Series"
QUEUED
127.0.0.1:6379(TX)> smembers tag
QUEUED
127.0.0.1:6379(TX)> exec
1) OK
2) "Mastering C++ in 21 days"
3) (integer) 2
4) 1) "C++ Programming"
   2) "Mastering Series"
```

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。

事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。

比如：

```
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> set a aaa
QUEUED
127.0.0.1:6379(TX)> set b bbb
QUEUED
127.0.0.1:6379(TX)> set c ccc
QUEUED
127.0.0.1:6379(TX)> exec
1) OK
2) OK
3) OK
```

如果在 set b bbb 处失败，set a 已成功不会回滚，set c 还会继续执行。

## 14.2 Redis 事务命令

下表列出了 redis 事务的相关命令：

| 序号  | 命令及描述                                                                         |
| --- | ----------------------------------------------------------------------------- |
| 1   | DISCARD<br>取消事务，放弃执行事务块内的所有命令。                                                |
| 2   | EXEC<br>执行所有事务块内的命令。                                                          |
| 3   | MULTI<br>标记一个事务块的开始。                                                          |
| 4   | UNWATCH<br>取消 WATCH 命令对所有 key 的监视。                                            |
| 5   | WATCH key [key ...]<br>监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。 |

# 15. Redis 脚本

## 15.1 Redis 脚本

Redis 脚本使用 Lua 解释器来执行脚本。 执行脚本的常用命令为 **EVAL**。

### 15.1.1 语法

Eval 命令的基本语法如下：

`127.0.0.1:6379> EVAL script numkeys key [key ...] arg [arg ...]`

### 15.1.2 实例

以下实例演示了 redis 脚本工作过程：

```
127.0.0.1:6379> eval "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}" 2 key1 key2 first second
1) "key1"
2) "key2"
3) "first"
4) "second"
```

## 15.2 Redis 脚本命令

下表列出了 redis 脚本常用命令：

| 序号  | 命令及描述                                                          |
| --- | -------------------------------------------------------------- |
| 1   | EVAL script numkeys key [key ...] arg [arg ...]<br>执行 Lua 脚本。  |
| 2   | EVALSHA sha1 numkeys key [key ...] arg [arg ...]<br>执行 Lua 脚本。 |
| 3   | SCRIPT EXISTS script [script ...]<br>查看指定的脚本是否已经被保存在缓存当中。      |
| 4   | SCRIPT FLUSH<br>从脚本缓存中移除所有脚本。                                  |
| 5   | SCRIPT KILL<br>杀死当前正在运行的 Lua 脚本。                               |
| 6   | SCRIPT LOAD script<br>将脚本 script 添加到脚本缓存中，但并不立即执行这个脚本。         |

# 16. Redis 连接

## 16.1 Redis 连接

Redis 连接命令主要是用于连接 redis 服务。

### 16.1.1 实例

以下实例演示了客户端如何通过密码验证连接到 redis 服务，并检测服务是否在运行：

```
127.0.0.1:6379> auth "123456"
OK
127.0.0.1:6379> ping
PONG
```

## 16.2 Redis 连接命令

下表列出了 redis 连接的基本命令：

| 序号  | 命令及描述                     |
| --- | ------------------------- |
| 1   | AUTH password<br>验证密码是否正确 |
| 2   | ECHO message<br>打印字符串     |
| 3   | PING<br>查看服务是否运行          |
| 4   | QUIT<br>关闭当前连接            |
| 5   | SELECT index<br>切换到指定的数据库 |

# 17. Redis 服务器

## 17.1 Redis 服务器

Redis 服务器命令主要是用于管理 redis 服务。

### 17.1.1 实例

以下实例演示了如何获取 redis 服务器的统计信息：

```
127.0.0.1:6379> info
# Server
redis_version:7.0.4
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:fe37830a1872c6d8
redis_mode:standalone
os:Linux 5.10.16.3-microsoft-standard-WSL2 x86_64
arch_bits:64
monotonic_clock:POSIX clock_gettime
multiplexing_api:epoll
atomicvar_api:c11-builtin
gcc_version:10.2.1
process_id:8786
process_supervised:no
run_id:d0928a00df4d6a82ef5a44e327874af50666605b
tcp_port:6379
server_time_usec:1663055676860577
uptime_in_seconds:17367
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:2111292
executable:/home/poo/redisfile/redis-7.0.4/src/./redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:8
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:1528992
used_memory_human:1.46M
used_memory_rss:14118912
used_memory_rss_human:13.46M
used_memory_peak:1607824
used_memory_peak_human:1.53M
used_memory_peak_perc:95.10%
used_memory_overhead:861864
used_memory_startup:859296
used_memory_dataset:667128
used_memory_dataset_perc:99.62%
allocator_allocated:1750008
allocator_active:2187264
allocator_resident:5324800
total_system_memory:8228069376
total_system_memory_human:7.66G
used_memory_lua:32768
used_memory_vm_eval:32768
used_memory_lua_human:32.00K
used_memory_scripts_eval:168
number_of_cached_scripts:1
number_of_functions:0
number_of_libraries:0
used_memory_vm_functions:32768
used_memory_vm_total:65536
used_memory_vm_total_human:64.00K
used_memory_functions:184
used_memory_scripts:352
used_memory_scripts_human:352B
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.25
allocator_frag_bytes:437256
allocator_rss_ratio:2.43
allocator_rss_bytes:3137536
rss_overhead_ratio:2.65
rss_overhead_bytes:8794112
mem_fragmentation_ratio:9.37
mem_fragmentation_bytes:12612808
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_total_replication_buffers:0
mem_clients_slaves:0
mem_clients_normal:1800
mem_cluster_links:0
mem_aof_buffer:0
mem_allocator:jemalloc-5.2.1
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
async_loading:0
current_cow_peak:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:6
rdb_bgsave_in_progress:0
rdb_last_save_time:1663053853
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_saves:4
rdb_last_cow_size:577536
rdb_last_load_keys_expired:0
rdb_last_load_keys_loaded:1
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_rewrites:0
aof_rewrites_consecutive_failures:0
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:12
total_commands_processed:114
instantaneous_ops_per_sec:0
total_net_input_bytes:5401
total_net_output_bytes:1539352
total_net_repl_input_bytes:0
total_net_repl_output_bytes:0
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
instantaneous_input_repl_kbps:0.00
instantaneous_output_repl_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:347
evicted_keys:0
evicted_clients:0
total_eviction_exceeded_time:0
current_eviction_exceeded_time:0
keyspace_hits:20
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
pubsubshard_channels:0
latest_fork_usec:1751
total_forks:4
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
total_active_defrag_time:0
current_active_defrag_time:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:21
dump_payload_sanitizations:0
total_reads_processed:140
total_writes_processed:148
io_threaded_reads_processed:0
io_threaded_writes_processed:0
reply_buffer_shrinks:12
reply_buffer_expands:0

# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:b3ff2b8c5f7688047f678d04327d9cd7d76c0bfa
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:12.936751
used_cpu_user:18.185174
used_cpu_sys_children:0.070588
used_cpu_user_children:0.006731
used_cpu_sys_main_thread:12.929884
used_cpu_user_main_thread:18.182301

# Modules

# Errorstats
errorstat_ERR:count=8
errorstat_NOAUTH:count=7
errorstat_WRONGPASS:count=1
errorstat_WRONGTYPE:count=5

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=8,expires=0,avg_ttl=0
```

## 17.2 Redis 服务器命令

下表列出了 redis 服务器的相关命令:

| 序号  | 命令及描述                                                              |
| --- | ------------------------------------------------------------------ |
| 1   | BGREWRITEAOF<br>异步执行一个 AOF（AppendOnly File） 文件重写操作                 |
| 2   | BGSAVE<br>在后台异步保存当前数据库的数据到磁盘                                       |
| 3   | CLIENT KILL [ip:port] [ID client-id]<br>关闭客户端连接                    |
| 4   | CLIENT LIST<br>获取连接到服务器的客户端连接列表                                    |
| 5   | CLIENT GETNAME<br>获取连接的名称                                          |
| 6   | CLIENT PAUSE timeout<br>在指定时间内终止运行来自客户端的命令                         |
| 7   | CLIENT SETNAME connection-name<br>设置当前连接的名称                        |
| 8   | CLUSTER SLOTS<br>获取集群节点的映射数组                                       |
| 9   | COMMAND<br>获取 Redis 命令详情数组                                         |
| 10  | COMMAND COUNT<br>获取 Redis 命令总数                                     |
| 11  | COMMAND GETKEYS<br>获取给定命令的所有键                                      |
| 12  | TIME<br>返回当前服务器时间                                                  |
| 13  | COMMAND INFO command-name [command-name ...]<br>获取指定 Redis 命令描述的数组 |
| 14  | CONFIG GET parameter<br>获取指定配置参数的值                                 |
| 15  | CONFIG REWRITE<br>对启动 Redis 服务器时所指定的 redis.conf 配置文件进行改写           |
| 16  | CONFIG SET parameter value<br>修改 redis 配置参数，无需重启                   |
| 17  | CONFIG RESETSTAT<br>重置 INFO 命令中的某些统计数据                             |
| 18  | DBSIZE<br>返回当前数据库的 key 的数量                                         |
| 19  | DEBUG OBJECT key<br>获取 key 的调试信息                                   |
| 20  | DEBUG SEGFAULT<br>让 Redis 服务崩溃                                     |
| 21  | FLUSHALL<br>删除所有数据库的所有key                                          |
| 22  | FLUSHDB<br>删除当前数据库的所有key                                           |
| 23  | INFO [section]<br>获取 Redis 服务器的各种信息和统计数值                           |
| 24  | LASTSAVE<br>返回最近一次 Redis 成功将数据保存到磁盘上的时间，以 UNIX 时间戳格式表示             |
| 25  | MONITOR<br>实时打印出 Redis 服务器接收到的命令，调试用                               |
| 26  | ROLE<br>返回主从实例所属的角色                                                |
| 27  | SAVE<br>同步保存数据到硬盘                                                  |
| 28  | SHUTDOWN [NOSAVE] [SAVE]<br>异步保存数据到硬盘，并关闭服务器                       |
| 29  | SLAVEOF host port<br>将当前服务器转变为指定服务器的从属服务器(slave server)            |
| 30  | SLOWLOG subcommand [argument]<br>管理 redis 的慢日志                     |
| 31  | SYNC<br>用于复制功能(replication)的内部命令                                   |

# 18. Redis GEO

Redis GEO 主要用于存储地理位置信息，并对存储的信息进行操作。

Redis GEO 操作方法有：

- geoadd：添加地理位置的坐标。
- geopos：获取地理位置的坐标。
- geodist：计算两个位置之间的距离。
- georadius：根据用户给定的经纬度坐标来获取指定范围内的地理位置集合。
- georadiusbymember：根据储存在位置集合里面的某个地点获取指定范围内的地理位置集合。
- geohash：返回一个或多个位置对象的 geohash 值。

## 18.1 geoadd

geoadd 用于存储指定的地理空间位置，可以将一个或多个经度(longitude)、纬度(latitude)、位置名称(member)添加到指定的 key 中。

geoadd 语法格式如下：

`GEOADD key longitude latitude member [longitude latitude member ...]`

以下实例中 key 为 Sicily，Palermo 和 Catania 为位置名称 ：

### 18.1.1 实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 1
127.0.0.1:6379> geodist sicily xian baoji
"158991.4724"
127.0.0.1:6379> georadius sicily 107 34 100 km
1) "baoji"
127.0.0.1:6379> georadius sicily 107 34 200 km
1) "baoji"
2) "xian"
```

## 18.2 geopos

geopos 用于从给定的 key 里返回所有指定名称(member)的位置（经度和纬度），不存在的返回 nil。

geopos 语法格式如下：

`GEOPOS key member [member ...]`

### 18.2.1 实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 0
127.0.0.1:6379> geopos sicily xian baoji nonexisting
1) 1) "108.96171838045120239"
   2) "34.27763623401597926"
2) 1) "107.23257333040237427"
   2) "34.33407180062865649"
3) (nil)
```

## 18.3 geodist

geodist 用于返回两个给定位置之间的距离。

geodist 语法格式如下：

`GEODIST key member1 member2 [m|km|ft|mi]`

member1 member2 为两个地理位置。

最后一个距离单位参数说明：

- m ：米，默认单位。

- km ：千米。

- mi ：英里。

- ft ：英尺。

### 18.3.1 实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 0
127.0.0.1:6379> geodist sicily xian baoji km
"158.9915"
127.0.0.1:6379> geodist sicily xian baoji mi
"98.7930"
127.0.0.1:6379> geodist sicily foo bar
(nil)
```

## 18.4 georadius、georadiusbymember

georadius 以给定的经纬度为中心， 返回键包含的位置元素当中， 与中心的距离不超过给定最大距离的所有位置元素。

georadiusbymember 和 GEORADIUS 命令一样， 都可以找出位于指定范围内的元素， 但是 georadiusbymember 的中心点是由给定的位置元素决定的， 而不是使用经度和纬度来决定中心点。

georadius 与 georadiusbymember 语法格式如下：

`GEORADIUS key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]`
`GEORADIUSBYMEMBER key member radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]`

参数说明：

- m ：米，默认单位。
- km ：千米。
- mi ：英里。
- ft ：英尺。
- WITHDIST: 在返回位置元素的同时， 将位置元素与中心之间的距离也一并返回。
- WITHCOORD: 将位置元素的经度和纬度也一并返回。
- WITHHASH: 以 52 位有符号整数的形式， 返回位置元素经过原始 geohash 编码的有序集合分值。 这个选项主要用于底层应用或者调试， 实际中的作用并不大。
- COUNT 限定返回的记录数。
- ASC: 查找结果根据距离从近到远排序。
- DESC: 查找结果根据从远到近排序。

### 18.4.1 georadius实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 0
127.0.0.1:6379> georadius sicily 107 34 200 km withdist
1) 1) "baoji"
   2) "42.8811"
2) 1) "xian"
   2) "183.2134"
127.0.0.1:6379> georadius sicily 107 34 200 km withcoord
1) 1) "baoji"
   2) 1) "107.23257333040237427"
      2) "34.33407180062865649"
2) 1) "xian"
   2) 1) "108.96171838045120239"
      2) "34.27763623401597926"
127.0.0.1:6379> georadius sicily 107 34 200 km withdist withcoord
1) 1) "baoji"
   2) "42.8811"
   3) 1) "107.23257333040237427"
      2) "34.33407180062865649"
2) 1) "xian"
   2) "183.2134"
   3) 1) "108.96171838045120239"
      2) "34.27763623401597926"
```

### 18.4.2 georadiusbymember实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 0
127.0.0.1:6379> geoadd sicily 108.86171582031249 34.37763636494646 "shendu"
(integer) 1
127.0.0.1:6379> georadiusbymember sicily shendu 100 km
1) "xian"
2) "shendu"
```

## 18.5 geohash

Redis GEO 使用 geohash 来保存地理位置的坐标。

geohash 用于获取一个或多个位置元素的 geohash 值。

geohash 语法格式如下：

`GEOHASH key member [member ...]`

### 18.5.1 实例

```
127.0.0.1:6379> geoadd sicily 108.96171582031249 34.27763636494646 "xian" 107.23257077026366 34.334072476228265 "baoji"
(integer) 0
127.0.0.1:6379> geohash sicily xian baoji
1) "wqj7p2p98n0"
2) "wqh724k6kn0"
```

# 19. Redis Stream

Redis Stream 主要用于消息队列（MQ，Message Queue），Redis 本身是有一个 Redis 发布订阅 (pub/sub) 来实现消息队列的功能，但它有个缺点就是消息无法持久化，如果出现网络断开、Redis 宕机等，消息就会被丢弃。

简单来说发布订阅 (pub/sub) 可以分发消息，但无法记录历史消息。

而 Redis Stream 提供了消息的持久化和主备复制功能，可以让任何客户端访问任何时刻的数据，并且能记住每一个客户端的访问位置，还能保证消息不丢失。

Redis Stream 的结构如下所示，它有一个消息链表，将所有加入的消息都串起来，每个消息都有一个唯一的 ID 和对应的内容：

![](https://www.runoob.com/wp-content/uploads/2020/09/en-us_image_0167982791.png)

每个 Stream 都有唯一的名称，它就是 Redis 的 key，在我们首次使用 xadd 指令追加消息时自动创建。

上图解析：

- **Consumer Group** ：消费组，使用 XGROUP CREATE 命令创建，一个消费组有多个消费者(Consumer)。
- **last_delivered_id** ：游标，每个消费组会有个游标 last_delivered_id，任意一个消费者读取了消息都会使游标 last_delivered_id 往前移动。
- **pending_ids** ：消费者(Consumer)的状态变量，作用是维护消费者的未确认的 id。 pending_ids 记录了当前已经被客户端读取的消息，但是还没有 ack (Acknowledge character：确认字符）。

**消息队列相关命令：**

- **XADD** - 添加消息到末尾
- **XTRIM** - 对流进行修剪，限制长度
- **XDEL** - 删除消息
- **XLEN** - 获取流包含的元素数量，即消息长度
- **XRANGE** - 获取消息列表，会自动过滤已经删除的消息
- **XREVRANGE** - 反向获取消息列表，ID 从大到小
- **XREAD** - 以阻塞或非阻塞方式获取消息列表

**消费者组相关命令：**

- **XGROUP CREATE** - 创建消费者组
- **XREADGROUP GROUP** - 读取消费者组中的消息
- **XACK** - 将消息标记为"已处理"
- **XGROUP SETID** - 为消费者组设置新的最后递送消息ID
- **XGROUP DELCONSUMER** - 删除消费者
- **XGROUP DESTROY** - 删除消费者组
- **XPENDING** - 显示待处理消息的相关信息
- **XCLAIM** - 转移消息的归属权
- **XINFO** - 查看流和消费者组的相关信息；
- **XINFO GROUPS** - 打印消费者组的信息；
- **XINFO STREAM** - 打印流信息

## 19.1 XADD

使用 XADD 向队列添加消息，如果指定的队列不存在，则创建一个队列，XADD 语法格式：

`XADD key ID field value [field value ...]`

- **key** ：队列名称，如果不存在就创建
- **ID** ：消息 id，我们使用 * 表示由 redis 生成，可以自定义，但是要自己保证递增性。
- **field value** ： 记录。

### 19.1.1 实例

```
127.0.0.1:6379> xadd mystream * name danny surname poo
"1663057924845-0"
127.0.0.1:6379> xadd mystream * field1 value1 field2 value2 field3 value3
"1663057947091-0"
127.0.0.1:6379> xlen mystream
(integer) 2
127.0.0.1:6379> xrange mystream - +
1) 1) "1663057924845-0"
   2) 1) "name"
      2) "danny"
      3) "surname"
      4) "poo"
2) 1) "1663057947091-0"
   2) 1) "field1"
      2) "value1"
      3) "field2"
      4) "value2"
      5) "field3"
      6) "value3"
```

## 19.2 XTRIM

使用 XTRIM 对流进行修剪，限制长度， 语法格式：

`XTRIM key MAXLEN [~] count`

- **key** ：队列名称
- **MAXLEN** ：长度
- **count** ：数量

### 19.2.1 实例

```
127.0.0.1:6379> xadd mystream * field1 a field2 b field3 c field4 d
"1663058033612-0"
127.0.0.1:6379> xtrim mystream maxlen 2
(integer) 1
127.0.0.1:6379> xrange mystream - +
1) 1) "1663057947091-0"
   2) 1) "field1"
      2) "value1"
      3) "field2"
      4) "value2"
      5) "field3"
      6) "value3"
2) 1) "1663058033612-0"
   2) 1) "field1"
      2) "a"
      3) "field2"
      4) "b"
      5) "field3"
      6) "c"
      7) "field4"
      8) "d"
```

## 19.3 XDEL

使用 XDEL 删除消息，语法格式：

`XDEL key ID [ID ...]`

- **key**：队列名称
- **ID** ：消息 ID

### 19.3.1  实例

```
127.0.0.1:6379> xadd dels* a 1
"1663058118107-0"
127.0.0.1:6379> xadd dels* b 2
"1663058121779-0"
127.0.0.1:6379> xadd dels* c 3
"1663058124718-0"
127.0.0.1:6379> xdel dels1663058118107-0
(integer) 1
127.0.0.1:6379> xrange dels- +
1) 1) "1663058121779-0"
   2) 1) "b"
      2) "2"
2) 1) "1663058124718-
```

## 19.4 XLEN

使用 XLEN 获取流包含的元素数量，即消息长度，语法格式：

`XLEN key`

- **key**：队列名称

### 19.4.1 实例

```
127.0.0.1:6379> xadd one * item 1
"1663058498514-0"
127.0.0.1:6379> xadd one * item 2
"1663058500332-0"
127.0.0.1:6379> xadd one * item 3
"1663058501745-0"
127.0.0.1:6379> xlen one
(integer) 30"
   2) 1) "c"
      2) "3"
```

## 19.4 XRANGE

使用 XRANGE 获取消息列表，会自动过滤已经删除的消息 ，语法格式：

`XRANGE key start end [COUNT count]`

- **key** ：队列名
- **start** ：开始值， - 表示最小值
- **end** ：结束值， + 表示最大值
- **count** ：数量

### 19.4.1 实例

```
127.0.0.1:6379> xadd poo * name san surname zhang
"1663058761922-0"
127.0.0.1:6379> xadd poo * name si surname li
"1663058766881-0"
127.0.0.1:6379> xadd poo * name wu surname wang
"1663058771073-0"
127.0.0.1:6379> xadd poo * name liu surname zhao
"1663058775323-0"
127.0.0.1:6379> xadd poo * name qi surname qian
"1663058779522-0"
127.0.0.1:6379> xlen poo
(integer) 5
127.0.0.1:6379> xrange poo - + count 2
1) 1) "1663058761922-0"
   2) 1) "name"
      2) "san"
      3) "surname"
      4) "zhang"
2) 1) "1663058766881-0"
   2) 1) "name"
      2) "si"
      3) "surname"
      4) "li"
```

## 19.5 XREVRANGE

使用 XREVRANGE 获取消息列表，会自动过滤已经删除的消息 ，语法格式：

`XREVRANGE key end start [COUNT count]`

- **key** ：队列名
- **end** ：结束值， + 表示最大值
- **start** ：开始值， - 表示最小值
- **count** ：数量

### 19.5.1 实例

```
127.0.0.1:6379> xadd pooo * name san surname zhang
"1663058873082-0"
127.0.0.1:6379> xadd pooo * name si surname li
"1663058876986-0"
127.0.0.1:6379> xadd pooo * name wu surname wang
"1663058881225-0"
127.0.0.1:6379> xadd pooo * name liu surname zhao
"1663058885297-0"
127.0.0.1:6379> xadd pooo * name qi surname qian
"1663058889769-0"
127.0.0.1:6379> xlen pooo
(integer) 5
127.0.0.1:6379> XREVRANGE pooo + - count 1
1) 1) "1663058889769-0"
   2) 1) "name"
      2) "qi"
      3) "surname"
      4) "qian"
```

## 19.6 XREAD

使用 XREAD 以阻塞或非阻塞方式获取消息列表 ，语法格式：

`XREAD [COUNT count] [BLOCK milliseconds] STREAMS key [key ...] id [id ...]`

- **count** ：数量
- **milliseconds** ：可选，阻塞毫秒数，没有设置就是非阻塞模式
- **key** ：队列名
- **id** ：消息 ID

### 19.6.1 实例

```
#从 Stream 头部读取两条消息
127.0.0.1:6379> xread count 2 streams mystream writers 0-0 0-0
1) 1) "mystream"
   2) 1) 1) "1663057947091-0"
         2) 1) "field1"
            2) "value1"
            3) "field2"
            4) "value2"
            5) "field3"
            6) "value3"
      2) 1) "1663058033612-0"
         2) 1) "field1"
            2) "a"
            3) "field2"
            4) "b"
            5) "field3"
            6) "c"
            7) "field4"
            8) "d"
2) 1) "writers"
   2) 1) 1) "1663058349732-0"
         2) 1) "name"
            2) "zhang"
            3) "xiao"
            4) "san"
      2) 1) "1663058356787-0"
         2) 1) "name"
            2) "li"
            3) "xiao"
            4) "si"
```

## 19.7 XGROUP CREATE

使用 XGROUP CREATE 创建消费者组，语法格式：

`XGROUP [CREATE key groupname id-or-$] [SETID key groupname id-or-$] [DESTROY key groupname] [DELCONSUMER key groupname consumername]`

- **key** ：队列名称，如果不存在就创建
- **groupname** ：组名。
- **$** ： 表示从尾部开始消费，只接受新消息，当前 Stream 消息会全部忽略。

从头开始消费:

`XGROUP CREATE mystream consumer-group-name 0-0`

从尾部开始消费:

`XGROUP CREATE mystream consumer-group-name $`

## 19.8 XREADGROUP GROUP

使用 XREADGROUP GROUP 读取消费组中的消息，语法格式：

`XREADGROUP GROUP group consumer [COUNT count] [BLOCK milliseconds] [NOACK] STREAMS key [key ...] ID [ID ...]`

- **group** ：消费组名
- **consumer** ：消费者名。
- **count** ： 读取数量。
- **milliseconds** ： 阻塞毫秒数。
- **key** ： 队列名。
- **ID** ： 消息 ID。

```
127.0.0.1:6379> XREADGROUP GROUP consumer-group-name consumer-name COUNT 1 STREAMS mystream >
1) 1) "mystream"
   2) 1) 1) "1663057947091-0"
         2) 1) "field1"
            2) "value1"
            3) "field2"
            4) "value2"
            5) "field3"
            6) "value3"
```

# 20. Redis 数据备份与恢复

## 20.1 Redis 数据备份

Redis **SAVE** 命令用于创建当前数据库的备份。

### 20.1.1 语法

redis Save 命令基本语法如下：

`127.0.0.1:6379> save`

### 20.1.2 实例

```
127.0.0.1:6379> save
20:M 14 Sep 2022 09:19:08.410 * DB saved on disk
OK
```

该命令将在 redis 安装目录中创建dump.rdb文件。

```
poo@poo:~/redisfile/redis-7.0.4/src$ ls *.rdb
dump.rdb
```

## 20.2 恢复数据

如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可以使用 **CONFIG** 命令，如下所示：

```
127.0.0.1:6379> config get dir
1) "dir"
2) "/home/poo/redisfile/redis-7.0.4/src"
```

以上命令 **config get dir** 输出的 redis 安装目录为 `/home/poo/redisfile/redis-7.0.4/s`。

## 20.3 Bgsave

创建 redis 备份文件也可以使用命令 **BGSAVE**，该命令在后台执行。

### 20.3.1 实例

```
127.0.0.1:6379> bgsave
Background saving started
```

# 21. Redis 安全

## 21.1 Redis 安全

我们可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。

### 21.1.1 实例

我们可以通过以下命令查看是否设置了密码验证：

```
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) ""
```

默认情况下 requirepass 参数是空的，这就意味着你无需通过密码验证就可以连接到 redis 服务。

你可以通过以下命令来修改该参数：

```
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) ""
127.0.0.1:6379> config set requirepass "123456"
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "123456"
```

设置密码后，客户端连接 redis 服务就需要密码验证，否则无法执行命令。

### 21.1.2 语法

**AUTH** 命令基本语法格式如下：

`127.0.0.1:6379> AUTH password`

### 21.1.3 实例

```
127.0.0.1:6379> auth "123456"
OK
127.0.0.1:6379> set mykey "test value"
OK
127.0.0.1:6379> get mykey
"test value"
```

# 22. Redis 性能测试

## 22.1 Redis 性能测试

Redis 性能测试是通过同时执行多个命令实现的。

### 22.1.1 语法

redis 性能测试的基本命令如下：

`redis-benchmark [option] [option value]`

**注意**：该命令是在 redis 的目录下执行的，而不是 redis 客户端的内部指令。

### 22.1.2 实例

以下实例同时执行 10000 个请求来检测性能：

```
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-benchmark -n 10000 -q -a "123456"
PING_INLINE: 90090.09 requests per second, p50=0.271 msec
PING_MBULK: 84033.61 requests per second, p50=0.295 msec
SET: 84745.77 requests per second, p50=0.295 msec
GET: 85470.09 requests per second, p50=0.279 msec
INCR: 91743.12 requests per second, p50=0.271 msec
LPUSH: 94339.62 requests per second, p50=0.263 msec
RPUSH: 86956.52 requests per second, p50=0.287 msec
LPOP: 99009.90 requests per second, p50=0.255 msec
RPOP: 99009.90 requests per second, p50=0.255 msec
SADD: 90090.09 requests per second, p50=0.279 msec
HSET: 90090.09 requests per second, p50=0.271 msec
SPOP: 89285.71 requests per second, p50=0.271 msec
ZADD: 90909.09 requests per second, p50=0.279 msec
ZPOPMIN: 84745.77 requests per second, p50=0.287 msec
LPUSH (needed to benchmark LRANGE): 93457.95 requests per second, p50=0.271 msec
LRANGE_100 (first 100 elements): 58823.53 requests per second, p50=0.439 msec
LRANGE_300 (first 300 elements): 24213.08 requests per second, p50=1.039 msec
LRANGE_500 (first 500 elements): 17035.78 requests per second, p50=1.471 msec
LRANGE_600 (first 600 elements): 14814.81 requests per second, p50=1.679 msec
MSET (10 keys): 119047.62 requests per second, p50=0.223 msec
```

redis 性能测试工具可选参数如下所示：

| 序号  | 选项                | 描述                                | 默认值       |
| --- | ----------------- | --------------------------------- | --------- |
| 1   | **-h**            | 指定服务器主机名                          | 127.0.0.1 |
| 2   | **-p**            | 指定服务器端口                           | 6379      |
| 3   | **-s**            | 指定服务器 socket                      |           |
| 4   | **-c**            | 指定并发连接数                           | 50        |
| 5   | **-n**            | 指定请求数                             | 10000     |
| 6   | **-d**            | 以字节的形式指定 SET/GET 值的数据大小           | 2         |
| 7   | **-k**            | 1=keep alive 0=reconnect          | 1         |
| 8   | **-r**            | SET/GET/INCR 使用随机 key, SADD 使用随机值 |           |
| 9   | **-P**            | 通过管道传输 <numreq> 请求                | 1         |
| 10  | **-q**            | 强制退出 redis。仅显示 query/sec 值        |           |
| 11  | **--csv**         | 以 CSV 格式输出                        |           |
| 12  | ***-l*（L 的小写字母）** | 生成循环，永久执行测试                       |           |
| 13  | **-t**            | 仅运行以逗号分隔的测试命令列表。                  |           |
| 14  | ***-I*（i 的大写字母）** | Idle 模式。仅打开 N 个 idle 连接并等待。       |           |

### 22.1.3 实例

以下实例我们使用了多个参数来测试 redis 性能：

```
poo@poo:~/redisfile/redis-7.0.4/src$ ./redis-benchmark -h 127.0.0.1 -p 6379 -t set,lpush -n 10000 -q -a "123456"
SET: 107526.88 requests per second, p50=0.239 msec
LPUSH: 91743.12 requests per second, p50=0.271 msec
```

以上实例中主机为 127.0.0.1，端口号为 6379，执行的命令为 set,lpush，请求数为 10000，通过 -q 参数让结果只显示每秒执行的请求数。

# 23. Redis 客户端连接

Redis 通过监听一个 TCP 端口或者 Unix socket 的方式来接收来自客户端的连接，当一个连接建立后，Redis 内部会进行以下一些操作：

- 首先，客户端 socket 会被设置为非阻塞模式，因为 Redis 在网络事件处理上采用的是非阻塞多路复用模型。
- 然后为这个 socket 设置 TCP_NODELAY 属性，禁用 Nagle 算法
- 然后创建一个可读的文件事件用于监听这个客户端 socket 的数据发送

## 23.1 最大连接数

maxclients 的默认值是 10000，你也可以在 redis.conf 中对这个值进行修改。

```
127.0.0.1:6379> config get maxclients
1) "maxclients"
2) "10000"
```

## 23.2 实例

以下实例我们在服务启动时设置最大连接数为 100000：

`redis-server --maxclients 100000`

## 23.3 客户端命令

| S.N. | 命令                 | 描述                            |
| ---- | ------------------ | ----------------------------- |
| 1    | **CLIENT LIST**    | 返回连接到 redis 服务的客户端列表          |
| 2    | **CLIENT SETNAME** | 设置当前连接的名称                     |
| 3    | **CLIENT GETNAME** | 获取通过 CLIENT SETNAME 命令设置的服务名称 |
| 4    | **CLIENT PAUSE**   | 挂起客户端连接，指定挂起的时间以毫秒计           |
| 5    | **CLIENT KILL**    | 关闭客户端连接                       |
