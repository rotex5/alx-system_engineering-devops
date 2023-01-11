# Client configuration file (w/ Puppet)

exec {'setting ssh_config policies':
  command  => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config'
  provider => 'shell'
}
