src     = []

component = aos_board_component('win32host', 'windows', src)

# Define the default component testcase set for this board
testcases = Split('''
    test/testcase/aosapi/api_test 
    test/testcase/basic_test 
    test/testcase/framework/alink_test 
    test/testcase/middleware/uagent/uota_test 
    test/testcase/framework/mqtt_test 
    test/testcase/network/netmgr_test 
    test/testcase/framework/wifi_hal_test 
    test/testcase/kernel/deviceIO_test 
    test/testcase/kernel/modules/fatfs_test
    test/testcase/kernel/modules/kv_test 
    test/testcase/network/umesh_test 
    test/testcase/kernel/rhino_test 
    test/testcase/osal_test 
    test/testcase/kernel/vfs_test 
    test/testcase/kernel/yloop_test 
    test/testcase/security/alicrypto_test 
    test/testcase/security/id2_test
    test/testcase/security/tls_test
    test/testcase/utility/cjson_test 
    test/testcase/utility/digest_algorithm_test 
    test/testcase/utility/hashtable_test 
''')

component.set_global_testcases(testcases)
aos_global_config.set('MESHLOWPOWER',1)
