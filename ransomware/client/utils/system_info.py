import platform
import socket
import os


def get_target_system_information():
    
    target_information = {
        "target_hostname" : socket.gethostname(),
        "target_machine_arch" : platform.machine(),
        "target_os_version": platform.version(),
        "target_platform" : platform.platform(),
        "target_user_info" : platform.uname(),
        "target_username": os.getenv("USERNAME"),
        "target_system" : platform.system(),
        "target_processor" : platform.processor(),
        }
    
    return target_information
    











