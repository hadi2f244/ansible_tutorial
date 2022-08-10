ansible all -m ping
# ansible all -m service -a "name=httpd state=started"
# ansible all -m shell -a "ping -c 3 1.1.1.1"
# ansible all -m -a "ping -c 3 1.1.1.1"
