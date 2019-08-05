# Puppet script to create ssh config file
file { '/home/vagrant/.ssh/config':
  mode    => '0600',
  content =>
  'Hostname 34.74.176.216
  HostName 34.74.176.216
  User ubuntu
  IdentityFile ~/.ssh/holberton
  PasswordAuthentication no
  ',
}
