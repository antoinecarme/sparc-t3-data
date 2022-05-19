Notes for later :

## IMPITOOL

These commands come from ipmitool/sunoem, sun version:

```
SETTING_FAN_MODE=1 ipmitool raw 46 65 1
SETTING_FAN_SPEED=25 ipmitool raw 46 32 25
```

Does not control the fans as expected, something missing ?

```


# ipmitool -U root -H poutou_SP -P changeme -v raw 0 0x2e 0x20 20
Running Get PICMG Properties my_addr 0x20, transit 0, target 0x20
Error response 0xc1 from Get PICMG Properities
Running Get VSO Capabilities my_addr 0x20, transit 0, target 0x20
Invalid completion code received: Invalid command
Discovered IPMB address 0x0
RAW REQ (channel=0x0 netfn=0x0 lun=0x0 cmd=0x2e data_len=2)
RAW REQUEST (2 bytes)
 20 14
Unable to send RAW command (channel=0x0 netfn=0x0 lun=0x0 cmd=0x2e rsp=0xc1): Invalid command
```

## Display the fan speed

```
# ipmitool -U root -H poutou_SP -P changeme sunoem cli "show /System/Cooling/Fans/Fan_0 fan_percentage"
Connected. Use ^D to exit.
-> show /System/Cooling/Fans/Fan_0 fan_percentage

  /System/Cooling/Fans/Fan_0
    Properties:
        fan_percentage = 41 %
```

```


# ipmitool -U root -H poutou_SP -P changeme sensor list | grep RPM
FB/FM0/F0/TACH   | 5000.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM0/F1/TACH   | 4200.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM1/F0/TACH   | 5100.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM1/F1/TACH   | 4300.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM2/F0/TACH   | 5200.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM2/F1/TACH   | 4300.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM3/F0/TACH   | 5100.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM3/F1/TACH   | 4300.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM4/F0/TACH   | 5000.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM4/F1/TACH   | 4300.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM5/F0/TACH   | 5000.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        
FB/FM5/F1/TACH   | 4200.000   | RPM        | ok    | 2400.000  | na        | na        | na        | na        | na        


```

## ILOM Restricted shell

credentials : root/changeme by default

A few linux commands are executable. 

```

-> set SESSION mode=Restricted

WARNING: The "Restricted Shell" account is provided solely
to allow Services to perform diagnostic tasks.

[(restricted_shell) poutou_SP:~]$ ls
bin/     log/     persist/
[(restricted_shell) poutou_SP:~]$ ls -la
drwxr-sr-x    3 root     8846           69 Feb 15  2018 ./
drwxr-sr-x   21 root     8846          169 Feb 15  2018 ../
-rw-r--r--    1 root     root           36 Feb 15  2018 .bash_logout
-rw-r--r--    1 root     root           31 Feb 15  2018 .bashrc
drwxr-sr-x    2 root     8846          565 Feb 15  2018 bin/
drwxrwxrwt    2 root     root          300 Sep  5 10:31 log/
drwxr-xr-x   15 root     root            0 Sep  5 11:02 persist/
[(restricted_shell) poutou_SP:~]$ ls -la /bin
outside restricted scope.
[(restricted_shell) poutou_SP:~]$ /bin/
[           dd          gzip        login       netstat     rmdir       true
bash        df          hostname    ls          pidof       run-parts   umount
bash-ilom   dmesg       ip          lsmod       pidof-ilom  sed         uname
busybox     echo        ipaddr      mkdir       ping        sh          usleep
cat         egrep       iplink      mknod       ping6       sleep       vi
chgrp       false       iproute     mktemp      ps          stat        zcat
chmod       fgrep       iprule      more        pwd         stty        
chown       getopt      iptunnel    mount       rbash       sync        
cp          grep        kill        mountpoint  readlink    tar        
date        gunzip      ln          mv          rm          touch      
[(restricted_shell) poutou_SP:~]$ /bin/

```

## fanctrl

In a restricted shell (need proper/non-restricted access first ;)

```
fanctrl usage:
(noargs)           = print current fan duty
-d percent = change fan duty to percent (do not use %%, just number)
```


