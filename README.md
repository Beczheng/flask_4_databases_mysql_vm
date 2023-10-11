# flask_4_databases_mysql_vm

### Assignment
- Course: HHA 504
- Homework assignment #5: Manually setting up and running a MySQL instance on a cloud VM.
  
### Summary of the assignment

#### 1. Create VM on Azure
- Login to your Microsoft Azure account.
- Click the navigation bar.
- Click `virtual machines`.
- Click `+create`.
- Click `azure virtual machine`.

| Tabs | Section | Steps |
| --- | --- | --- | 
| Basics | Project details | Create a new resource group for "resource group". |
| Basics | Instance details | - Create a new name for the virtual machine for "virtual machine name". - Then, select `(US) East US` for "region". Then, select `standard` for security type. After, select `Ubuntu Server 20/04 LTS - x64 Gen2Lastly` for "image". Lastly, click `see all sizes` and select `B1ms` for "sizes". |
| Basics | Administrator account | For "authentication type", select `password`. Create your own username and password. |
| Basics | Inbound port rules | For "select inbound ports", select `HTTP(80)` and `HTTPS(443)`. |
| Networking | Network interface | Click `delete public IP and NIC when VM is deleted`. |
| Networking | Auto-shutdown | Click `enable auto-shutdown`. For "shutdown time", type `11:59:00 PM`. For "time zone", select `(UTC-05:00) Eastern Time (US & Canada)`. |
| Review + create | | When reviewing the VM, it should say `1 X Standard B1ms by Microsoft` and `0.0207 USD/hr`. |


