# Use Netmiko to change the logging buffer size (logging buffered <size>)
# and to disable console logging (no logging console)
# from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
from getpass import getpass
from netmiko import ConnectHandler


def main():

    password = getpass()

    pynet_rtr1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 22}
    pynet_rtr2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}

    for ssh in pynet_rtr1, pynet_rtr2:
        ssh_connection = ConnectHandler(**ssh)
        ssh_connection.config_mode()
        ssh_connection.send_config_from_file(config_file='commands_file.txt')

        output = ssh_connection.send_command('show run | inc logging')
        hostname = ssh_connection.send_command('show run | inc hostname pynet').split()

        print '*' * 10 + " New logging configurations for Cisco router %s " % hostname[1] + '*' * 10
        print output
        print '*' * 76

if __name__ == "__main__":
    main()