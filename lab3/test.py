import libvirt
conn=libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain=conn.lookupByID(id)
    print(id)
    print(domain.name())
    print("max memory: %d KB" %domain.info()[1])
    print("number of CPU(s): %d "%domain.info()[3])
    