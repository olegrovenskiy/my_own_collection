# Ansible Collection - my_own_collection.my_own_module

Documentation for the collection.
Tag 1.0.0 - initial
Tag 1.0.1 - collection with tar.gz

Module: My_Own_module

For idempotent done next:

1. Check if the file exist
2. If Yes, nothing to do
3. If No, create new file and write content

    import os.path
    check_file = os.path.exists(module.params['path'])
    if check_file == True:
       result['changed'] = False
       result['mesage'] = 'file was before'
       result['original_mesage'] = 'original'
    else:
       with open(module.params['path'], 'w') as  some_file:
         some_file.write(module.params['content'])
       result['changed'] = True
       result['mesage'] = 'file was created'
       result['original_mesage'] = 'original'

