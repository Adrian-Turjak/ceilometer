
""""Mapping of Nova VM states to ints for use in metering. """
# It might be better to build a query for this list in
# the NoveClient rather than store it here.
# Or import vm_states and use the names defined there.
states = {'active': 1,
          'building': 2,
          'paused': 3,
          'suspended': 4,
          'stopped': 5,
          'rescued': 6,
          'resized': 7,
          'soft_deleted': 8,
          'deleted': 9,
          'error': 10,
          'shelved': 11,
          'shelved_offloaded': 12}