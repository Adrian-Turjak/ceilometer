from nova.compute import vm_states as vms

""""Mapping of Nova VM states to ints for use in metering. """
# It might be better to build a query for this list in
# the NoveClient rather than store it here.
states = {vms.ACTIVE: 1,
          vms.BUILDING: 2,
          vms.PAUSED: 3,
          vms.SUSPENDED: 4,
          vms.STOPPED: 5,
          vms.RESCUED: 6,
          vms.RESIZED: 7,
          vms.SOFT_DELETED: 8,
          vms.DELETED: 9,
          vms.ERROR: 10,
          vms.SHELVED: 11,
          vms.SHELVED_OFFLOADED: 12}
