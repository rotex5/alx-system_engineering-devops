#  Install Nginx web server (w/ Puppet)

exec { 'update packages':
  command  => 'apt-get update',
  provider => 'shell',
}

exec { 'add nginx stable repo':
  command  => 'sudo add-apt-repository ppa:nginx/stable',
  provider => 'shell',
}

package { 'install nginx':
  ensure => 'installed',
}

exec { 'grant user rights to edit folder':
  command  => 'sudo chown -R "$USER:$USER" /var/www',
  provider => 'shell',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}


file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}

exec { 'restart service':
  command  => 'service nginx restart',
  provider => 'shell',
}


service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
