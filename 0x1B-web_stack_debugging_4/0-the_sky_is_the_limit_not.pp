# Fix the number of max open files per process

exec {'fix nginx and restart':
command => "sudo sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart",
path    => ['/usr/bin', '/bin'],
}
