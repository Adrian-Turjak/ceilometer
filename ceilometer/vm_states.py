from nova.compute import vm_states as vm

""""Mapping of Nova VM states to ints for use in metering. """
states = {vm.ACTIVE: 1,
          vm.BUILDING: 2,
          vm.PAUSED: 3,
          vm.SUSPENDING: 4,
          vm.STOPPED: 5,
          vm.RESCUED: 6,
          vm.RESIZED: 7,
          vm.SOFT_DELETED: 8,
          vm.DELETED: 9,
          vm.ERROR: 10,
          vm.SHELVED: 11,
          vm.SHELVED_OFFLOADED: 12}
