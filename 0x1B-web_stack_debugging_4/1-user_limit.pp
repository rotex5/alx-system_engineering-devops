# Fix for opening many files

exec {'fix-1':
  command => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}

exec {'fix-2':
  command => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
