# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

file_line { '/etc/nginx/sites-available/default':
  ensure => 'present',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# service { 'nginx_stop':
#   ensure  => stopped,
#   enable  => true,
#   require => Package['nginx'],
# }

# file_line { 'Add redirection, 301':
#   ensure   => 'present',
#   path     => '/etc/nginx/sites-available/default',
#   after    => 'listen 80 default_server;',
#   multiple => true,
#   line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
# }


# file { '/var/www/html/index.html':
#   mode    => '0744',
#   content => 'Holberton School',
# }


# service { 'nginx':
#   ensure  => running,
#   enable  => true,
#   require => Package['nginx'],
# }
