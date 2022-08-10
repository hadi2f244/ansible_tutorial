ansible-vault encrypt_string "pass123" --ask-vault-pass 
ansible-vault encrypt_string --ask-vault-pass --name "ansible_become_pass" 'my_root_pass'
ansible-vault encrypt_string "pass123" --vault-password-file=.vault_pass --encrypt-vault-id default
