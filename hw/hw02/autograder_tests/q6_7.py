test = {   'name': 'q6_7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like your table '
                                               "doesn't have all 3 columns "
                                               'that are;\n'
                                               '>>> # in the inventory '
                                               'table.;\n'
                                               '>>> '
                                               'remaining_inventory.num_columns\n'
                                               '3',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> #It looks like you forgot '
                                               'to subtract off the sales.;\n'
                                               '>>> '
                                               'remaining_inventory.column("count").item(0) '
                                               '!= 45\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'remaining_inventory.where(1, '
                                               "'grape')\n"
                                               'box ID | fruit name | count\n'
                                               '57930  | grape      | 162',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
