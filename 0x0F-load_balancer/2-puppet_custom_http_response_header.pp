# automate the task of creating a custom HTTP header response, but with Puppet.
include stdlib

$link = 'https://www.youtube.com/watch?v=PCfiqY05BpA'
$content = "\trewrite ^/redirect_me/$ ${link} permanent;"
$custom_header = "add_header X-Served-By \$hostname;"

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec {'install Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}


file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $content,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}

file_line { 'Set X-Served-By header':
  ensure   => 'present',
  after    => 'http {',
  path     => '/etc/nginx/nginx.conf',
  multiple => true,
  line     => $custom_header,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}
