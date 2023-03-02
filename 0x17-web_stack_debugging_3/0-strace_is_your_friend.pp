# incorrect file extention
exec{ 'fix-extention':
    command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
}
