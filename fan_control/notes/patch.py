## 
## Process used to make a sparc T3-1 more silent by customizing the latest firmware in order to use it as a home server.
## This script will be used to reassemble the new firmware after the necessary changes have been made.
##
## 
## 
## STEP 0 : Disassemble the firmware
## 
## binwalk -e Firmware.pkg
## ==> the largest/root sqaushfs filesystem is at offest 0x20E420
## ==> fs images in dir  _Firmware.pkg.extracted/
## cd _Firmware.pkg.extracted/
## Change the needed files in squashfs-root-0 (largest directory)
##
##
## STEP 1 : Fan default  config
## 
## adapt fan control default config : set fan mode to fixed and set the speed to 30 by default. The speed can be controlled with '/usr/local/bin/fanctrl -d 20' for example.
## 
## vi squashfs-root-0/etc/static_conf/ifc_config.conf
## diff squashfs-root-0/etc/static_conf/ifc_config.conf squashfs-root-0/etc/static_conf/ifc_config.conf
## 6c6
## < ALGO_TYPE 0
## ---
## > ALGO_TYPE 1
## 133c133
## <    FAN_SPEED 60
## ---
## >    FAN_SPEED 30
##
##
##  STEP 2 : Add a few changes to escape the rbash restricted shell
##
## Add some executables to /home/ruser/bin/
## cd ./squashfs-root-0/home/ruser/bin/
## ln -sf ../../../bin/cp
## ln -sf ../../../bin/vi
## ln -sf ../../../bin/ln
## ln -sf ../../../bin/grep
## ln -sf ../../../alt-bin/bash
## ln -sf ../../../usr/local/bin/fanctrl   --> usage : 
## fanctrl
## fanctrl usage:
## (noargs)           = print current fan duty
## -d percent = change fan duty to percent (do not use %%, just number)
## d:p:
## /dev/fanctrl0
##
##
##
## STEP 3 : Rebuild the root image
##
## mksquashfs squashfs-root-0 20E420-1.squashfs -noappend -always-use-fragments
## 
## 
## 
## STEP 4 : Run this python script to reassemble the firmware
##
## cd ../../
## python3 patch.py
## ==> new firmware under Firmware_patched.pkg


def patch_binary_file(source, target, start, end, output):
    with open(source, mode='rb') as file1:
        sourceContent = file1.read()
    with open(target, mode='rb') as file2:
        targetContent = file2.read()
    position2 = start
    position3 = end
    zero_filler = bytearray(position3 - position2 - len(targetContent))
    sourceContent2 = sourceContent[:position2] + targetContent + zero_filler + sourceContent[position3:]
    print("POSITIONS", (len(sourceContent) , len(targetContent), start , end, position2, position3, len(sourceContent2)))

    with open(output, mode='wb') as file3:
        file3.write(sourceContent2)
        

lSource = "Sun_System_Firmware-8_3_40_a-SPARC_T3-1.pkg"
lOutput = "Sun_System_Firmware-8_3_40_a-SPARC_T3-1_patched.pkg"
# modified file with lower fan speeds
lTarget = "_Sun_System_Firmware-8_3_40_a-SPARC_T3-1.pkg.extracted/20E420-1.squashfs"
patch_binary_file(lSource, lTarget , 0x20E420, 0xF4B420, lOutput)
