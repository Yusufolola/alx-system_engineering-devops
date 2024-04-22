#SSH configuration file so that you can connect to a server 
#without typing a password

file {'No_password':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file {'ssh_config_identity':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school'
}
