# automate the task of creating a custom HTTP header response, but with Puppet.
include stdlib

$link = "/etc/nginx/sites-available/default"
$custom_header = "add_header X-Served-By \$HOSTNAME;"

exec { 'exec commands':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a $custom_header;" $link;
  service nginx restart',
  provider => shell,
}
