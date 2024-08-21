# This manuscript increases the amount of traffic an Nginx server can handle

# Increase ULIMIT of the default file
exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' \
/etc/default/nginx;\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}
