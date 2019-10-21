---
title: 【已解决】Ubuntu无法通过WPA连接WiFi
date: 2019-10-21 10:37:24
tags: Ubuntu
category: 教程
---

1. 安装wpa相关的package

```bash
sudo apt install wpasupplicant
```

2. 使用wpa生产配置文件

```bash
wpa_passphrase your_SSID
# reading passphrase from stdin
your_passowrd
network={
	ssid="your_SSID"
	#psk="your_passowrd"
	psk=9b16759eb50227bdad9cb3b313afd6ed4975d9a8422c71f1acda73af224c222f
}
```

3. 将生成的psk写入`/etc/wpa_supplicant.conf`

```
network={
	ssid="your_SSID"
	#psk="your_passowrd"
	psk=9b16759eb50227bdad9cb3b313afd6ed4975d9a8422c71f1acda73af224c222f
}
```

4. 进行连接

```bash
sudo wpa_supplicant -i your_SSID -c /etc/wpa_supplicant.conf
```

此时还是连接错误

```bash
Successfully initialized wpa_supplicant
wlan0: Trying to associate with xx:xx:xx:xx:xx:xx (SSID='WLAN-XXXX' freq=2412 MHz)
wlan0: Associated with xx:xx:xx:xx:xx:xx
wlan0: CTRL-EVENT-DISCONNECTED bssid=xx:xx:xx:xx:xx:xx reason=0 locally_generated=1
wlan0: WPA: 4-Way Handshake failed - pre-shared key may be incorrect
wlan0: CTRL-EVENT-SSID-TEMP-DISABLED id=0 ssid="WLAN-XXXX" auth_failures=1 duration=10 reason=WRONG_KEY
wlan0: CTRL-EVENT-REGDOM-CHANGE init=CORE type=WORLD
wlan0: CTRL-EVENT-ASSOC-REJECT status_code=1
wlan0: Reject scan trigger since one is already pending
wlan0: Failed to initiate AP scan
wlan0: Reject scan trigger since one is already pending
wlan0: Failed to initiate AP scan
wlan0: Reject scan trigger since one is already pending
wlan0: Failed to initiate AP scan
wlan0: CTRL-EVENT-SCAN-FAILED ret=-16 retry=1
wlan0: CTRL-EVENT-SSID-REENABLED id=0 ssid="WLAN-XXXX"
wlan0: Trying to associate with xx:xx:xx:xx:xx:xx (SSID='WLAN-XXXX' freq=2412 MHz)
wlan0: Associated with xx:xx:xx:xx:xx:xx
```

这里是Ubuntu下的一个[Bug](https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/1681513)，需要修改network-manager的参数

```bash
sudo vim /etc/NetworkManager/NetworkManager.conf
```

写入

```
[device]
wifi.scan-rand-mac-address=no
```

5. 重启

```bash
sudo reboot
```

6. 重新连接

```
sudo wpa_supplicant -i your_SSID -c /etc/wpa_supplicant.conf
```

7. DHCP

```bash
sudo dhcp -v <your_wifi_device>
```

WiFi设备接口可通过`ip a`或者`ifconfig`获取