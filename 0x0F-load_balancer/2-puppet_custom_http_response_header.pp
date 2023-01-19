# automate the task of creating a custom HTTP header response, but with Puppet.

include stdlib

$custom_header = "add_header X-Served-By \$hostname;"

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}


exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}


file_line { 'Insert X-Served-By header':
  ensure   => 'present',
  after    => 'http {',
  path     => '/etc/nginx/nginx.conf',
  multiple => true,
  line     => $custom_header,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.nginx-debian.html']
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
