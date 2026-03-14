## 1.补充信息：

1. EasyCli报错：

   这里填写了base-url, api-key点击右下角的apply后，出现“**Failed to apply 1 setting(s)**”红字；

   查看CPA的日志：[2026-03-13 00:45:15] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/claude-api-key"
   [2026-03-13 00:45:15] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/codex-api-key"
   [2026-03-13 00:45:16] [--------] [info ] [gin_logger.go:93] 200 |         602ms |  178.128.111.13 | GET     "/v0/management/gemini-api-key"
   [2026-03-13 00:45:16] [--------] [info ] [gin_logger.go:93] 200 |         706ms |  178.128.111.13 | GET     "/v0/management/codex-api-key"
   [2026-03-13 00:45:16] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/config"
   [2026-03-13 00:45:16] [--------] [info ] [gin_logger.go:93] 200 |         982ms |  178.128.111.13 | GET     "/v0/management/claude-api-key"
   [2026-03-13 00:45:17] [--------] [info ] [gin_logger.go:93] 200 |         240ms |  178.128.111.13 | GET     "/v0/management/config"
   [2026-03-13 00:45:17] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/codex-api-key"
   [2026-03-13 00:45:17] [--------] [error] [gin_logger.go:89] 500 |         260ms |  178.128.111.13 | PUT     "/v0/management/codex-api-key"
   [2026-03-13 00:48:58] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/auth-files"
   [2026-03-13 00:48:58] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/claude-api-key"
   [2026-03-13 00:48:58] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/auth-files"
   [2026-03-13 00:48:58] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/codex-api-key"
   [2026-03-13 00:48:58] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/gemini-api-key"
   [2026-03-13 00:48:59] [--------] [info ] [gin_logger.go:93] 200 |        1.192s |  178.128.111.13 | GET     "/v0/management/codex-api-key"
   [2026-03-13 00:48:59] [--------] [info ] [gin_logger.go:93] 200 |        1.101s |  178.128.111.13 | GET     "/v0/management/auth-files"
   [2026-03-13 00:48:59] [--------] [info ] [gin_logger.go:93] 200 |        1.197s |  178.128.111.13 | GET     "/v0/management/gemini-api-key"
   [2026-03-13 00:49:00] [--------] [info ] [gin_logger.go:93] 200 |        1.101s |  178.128.111.13 | GET     "/v0/management/claude-api-key"
   [2026-03-13 00:49:00] [--------] [info ] [gin_logger.go:93] 200 |         317ms |  178.128.111.13 | GET     "/v0/management/auth-files"
   [2026-03-13 00:49:44] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/config"
   [2026-03-13 00:49:45] [--------] [info ] [gin_logger.go:93] 200 |         293ms |  178.128.111.13 | GET     "/v0/management/config"
   [2026-03-13 00:49:45] [--------] [info ] [gin_logger.go:93] 204 |            0s |  178.128.111.13 | OPTIONS "/v0/management/codex-api-key"
   [2026-03-13 00:49:45] [--------] [error] [gin_logger.go:89] 500 |         262ms |  178.128.111.13 | PUT     "/v0/management/codex-api-key"

2. EasyCli连接信息：

   1. base-url: https://ai.hybgzs.com 这个链接, api-key不用说了，这个绝对可以用的，一直使用这个CCSwitch里写的有，没问题;

3. VPS中的config.yaml:

   ```yaml
   port: 8317
   remote-management:
     allow-remote: true
     secret-key: "magecXXXXXXX314"
     disable-control-panel: false
   auth-dir: "/data/auths"
   debug: false
   logging-to-file: false
   usage-statistics-enabled: false
   request-retry: 3
   quota-exceeded:
     switch-project: true
     switch-preview-model: true
   api-keys:
     - "maXXXXXXXX910"
   ```

4. VPS上的CliProxyAPI显示日志有启动成功，状态：Pod对应的status：Active, network对应显示Available. 且EasyCli连上也没问题，通过上面的这个secret-key。

5. 这个问题不太清楚。

## 2.执行CURL:

```
curl -X PUT \
-H "Content-Type: application/json" \
-H "Authorization: Bearer magXXXXXXXXXX314" \
-d '[{"api-key":"sk-NYVNzxj7XVaQCGxxxxxxxxxxxxxxxxNM2RQ", "base-url":"https://ai.hybgzs.com"}]' \
http://127.0.0.1:8317/v0/management/codex-api-key 
```

> 结果为：
> {"error":"failed to save config: open /data/config.yaml: read-only file system"}/CLIProxyAPI # 

## 3.可写性

- 应该第二种其中一个，因为看到了Podname,以及：.kubernetes.io/pod-index=0内容；
- 部署方式：在clawcloud里面创建时，有填写镜像名等参数，然后开始创建，里面会配置config.yaml，属于什么方式？感觉和之前的compose拉取镜像类似，但不完全相同；
- data: /data, 根目录下的；
-  readOnlyRootFilesystem：没设置，除非有默认或其他意外情况。
- 可看到的文件读写权限：
  - /data # ls -la
    total 32
    drwxr-xr-x    5 root     root          4096 Mar 12 22:26 .
    drwxr-xr-x    1 root     root            93 Mar 12 22:26 ..
    drwxr-xr-x    2 root     root          4096 Mar 12 22:26 auths
    -rw-r--r--    1 root     root           332 Mar 12 22:26 config.yaml
    drwx------    2 root     root         16384 Mar 12 21:49 lost+found
    drwxr-xr-x    2 root     root          4096 Mar 12 22:26 static
  - /data/static # ls -al
    total 2128
    drwxr-xr-x    2 root     root          4096 Mar 12 22:26 .
    drwxr-xr-x    5 root     root          4096 Mar 12 22:26 ..
    -rw-r--r--    1 root     root       2167175 Mar 12 22:26 management.html
  - /CLIProxyAPI # ls -la
    total 37880
    -rw-r--r--    1 root     root             0 Mar 13 01:52 -H
    -rw-r--r--    1 root     root             0 Mar 13 01:52 -d
    drwxr-xr-x    1 root     root            26 Mar 13 01:52 .
    drwxr-xr-x    1 root     root            93 Mar 12 22:26 ..
    -rwxr-xr-x    1 root     root      38764706 Mar 10 19:10 CLIProxyAPI
    -rw-r--r--    1 root     root         16462 Mar 10 19:09 config.example.yaml
- 验证结果：
  - /CLIProxyAPI # test -w /data && echo writable || echo readonly
    writable
    /CLIProxyAPI # mount | grep /data 或 cat /proc/mounts | grep /data
    grep: 或: No such file or directory
    grep: cat: No such file or directory
    /proc/mounts:/dev/mapper/vg_lvm-pvc--67c1ce19--e546--4512--91e6--0c3eb803f4cf /data ext4 rw,relatime 0 0
    /proc/mounts:/dev/mapper/vg_kubernetes-lv_kubelet /data/config.yaml xfs ro,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota 0 0