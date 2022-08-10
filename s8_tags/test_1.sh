ansible-playbook main_1.yaml -t "myrole"
ansible-playbook main_1.yaml -t "myrole2"
ansible-playbook main_1.yaml -t "myrole,myrole2"
ansible-playbook main_1.yaml -t "show-variable"
ansible-playbook main_1.yaml -t "copy-files"
ansible-playbook main_1.yaml --skip-tags "myrole"

