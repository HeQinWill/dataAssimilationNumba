# dataAssimilationNumba
想要利用numba加速资料同化的程序 
已经成功clone，接下来尝试同步到github 
github已经收到 
接下来测试pull到本地
```shell
heqin@heqin-dell:~$ git config --global user.email "Will.He@outlook.com"
heqin@heqin-dell:~$ git config --global user.name "HeQin-Dell"
```
```shell
heqin@heqin-dell:~$ mkdir ~/Documents/forGithub
heqin@heqin-dell:~$ cd ~/Documents/forGithub
heqin@heqin-dell:~/Documents/forGithub$ git clone https://github.com/HeQinWill/dataAssimilationNumba
Cloning into 'dataAssimilationNumba'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
```shell

若只想在本地使用的话
在vscode中点击add，新建一个目录如github（名字可以自己取），将其初始化，然后就可以stage在commit

```shell
heqin@heqin-dell:~$ source activate ncl-6.5.0
(ncl-6.5.0) heqin@heqin-dell:~$ apt install ncview
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?
(ncl-6.5.0) heqin@heqin-dell:~$ sudo apt install ncview
[sudo] password for heqin: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libaec0 libhdf5-10 libnetcdf11 libsz2 libudunits2-0
The following NEW packages will be installed:
  libaec0 libhdf5-10 libnetcdf11 libsz2 libudunits2-0 ncview
0 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
Need to get 1,804 kB of archives.
After this operation, 7,551 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 libaec0 amd64 0.3.2-1 [18.0 kB]
Get:2 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 libsz2 amd64 0.3.2-1 [5,048 B]
Get:3 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 libhdf5-10 amd64 1.8.16+docs-4ubuntu1 [995 kB]
Get:4 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 libnetcdf11 amd64 1:4.4.0-2 [286 kB]
Get:5 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 libudunits2-0 amd64 2.2.20-1 [69.5 kB]
Get:6 https://mirrors.ustc.edu.cn/ubuntu xenial/universe amd64 ncview amd64 2.1.6+ds-1build1 [430 kB]
Fetched 1,804 kB in 1s (964 kB/s)
Selecting previously unselected package libaec0:amd64.
(Reading database ... 259177 files and directories currently installed.)
Preparing to unpack .../libaec0_0.3.2-1_amd64.deb ...
Unpacking libaec0:amd64 (0.3.2-1) ...
Selecting previously unselected package libsz2:amd64.
Preparing to unpack .../libsz2_0.3.2-1_amd64.deb ...
Unpacking libsz2:amd64 (0.3.2-1) ...
Selecting previously unselected package libhdf5-10:amd64.
Preparing to unpack .../libhdf5-10_1.8.16+docs-4ubuntu1_amd64.deb ...
Unpacking libhdf5-10:amd64 (1.8.16+docs-4ubuntu1) ...
Selecting previously unselected package libnetcdf11.
Preparing to unpack .../libnetcdf11_1%3a4.4.0-2_amd64.deb ...
Unpacking libnetcdf11 (1:4.4.0-2) ...
Selecting previously unselected package libudunits2-0:amd64.
Preparing to unpack .../libudunits2-0_2.2.20-1_amd64.deb ...
Unpacking libudunits2-0:amd64 (2.2.20-1) ...
Selecting previously unselected package ncview.
Preparing to unpack .../ncview_2.1.6+ds-1build1_amd64.deb ...
Unpacking ncview (2.1.6+ds-1build1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for install-info (6.1.0.dfsg.1-5) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up libaec0:amd64 (0.3.2-1) ...
Setting up libsz2:amd64 (0.3.2-1) ...
Setting up libhdf5-10:amd64 (1.8.16+docs-4ubuntu1) ...
Setting up libnetcdf11 (1:4.4.0-2) ...
Setting up libudunits2-0:amd64 (2.2.20-1) ...
Setting up ncview (2.1.6+ds-1build1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
```

