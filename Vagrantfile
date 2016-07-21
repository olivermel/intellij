# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.

  # create intellij node (change this to new project)
    
 config.vm.define :intellij do |intellij_config|

     #intellij_config.vm.box = "bento/centos-6.7"
     intellij_config.vm.box = "cyplo/centos-6.5-gui"
     intellij_config.vm.hostname = "intellij"
     intellij_config.vm.network :private_network, ip: "192.168.1.22"
     intellij_config.vm.provider "virtualbox" do |vb|
     intellij_config.ssh.forward_agent = true
     intellij_config.ssh.forward_x11 = true
     end
     intellij_config.vm.provision :shell, path: "bootstrap.sh", privileged: false
 end

end
