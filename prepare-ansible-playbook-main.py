# 1 command line parameter the port number is needed
# utility then gets the subutai container ip addresses
# adds them to the main play book which at the end might look like this
#     minio_server_cluster_nodes:
#      - 'http://172.31.234.4:9091/minio-data'
#      - 'http://172.28.234.3:9091/minio-data'

import re
import sys
iplist = [re.findall('ansible_ssh_host=.*',line)
        for line in open('/etc/ansible/minio-master.hosts')]
if iplist:
        with open("ansible-playbook-main.yml", "a") as myfile:
                for item in iplist:
                        if len(item) > 0:
                                ip = item[0].replace("ansible_ssh_host=", "")
                                myfile.write("      - 'http://" + ip + ":" + sys.argv[1] + "/minio-data'")
                                myfile.write("\n")
                myfile.close()
