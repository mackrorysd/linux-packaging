VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  #config.vm.provider "virtualbox" do |v|
  #  v.customize ["modifyvm", :id, "--memory", "4096"]
  #  v.customize ["modifyvm", :id, "--cpus", "4"]
  #end

  config.vm.define :deb do |deb|
    deb.vm.box = "deb"
    config.vm.synced_folder "./", "/home/vagrant/linux-packaging"
  end
  config.vm.define :rpm do |rpm|
    rpm.vm.box = "rpm"
    config.vm.synced_folder "./", "/home/vagrant/linux-packaging"
  end

end
