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
| Basics | Project details | For "resource group", create a new resource group. |
| Basics | Instance details | For "virtual machine name", create a new name for the VM. For "region", select `(US) East US`. For "security type", select `standard`. For "size", click `see all sizes` and select `B1ms`. |
| Basics | Administrator account | For "authentication type", select `password`. Create your own username and password. |
| Basics | Inbound port rules | For "select inbound ports", select `HTTP(80)` and `HTTPS(443)`. |
| Networking | Network interface | Click `delete public IP and NIC when VM is deleted`. |
| Networking | Auto-shutdown | Click `enable auto-shutdown`. For "shutdown time", type `11:59:00 PM`. For "time zone", select `(UTC-05:00) Eastern Time (US & Canada)`. |
| Review + create | | When reviewing the VM, it should say `1 X Standard B1ms by Microsoft` and `0.0207 USD/hr`. |


