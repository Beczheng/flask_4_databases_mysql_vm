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
| Basics | Project details | For *resource group*, create a new resource group. |
| Basics | Instance details | For *virtual machine name*, create a new virtual machine name. Then, for *region*, select `(US) East US`. Then, for *security type*, select `standard`. After, for *image*, select `Ubuntu Server 20/04 LTS - x64 Gen2Lastly`. Lastly, for *sizes*, click `see all sizes` and select `B1ms`. |
| Basics | Administrator account | For *authentication type*, select `password`. Then, create a username and password. |
| Basics | Inbound port rules | For *select inbound ports*, select `HTTP(80)` and `HTTPS(443)`. |
| Networking | Network interface | Click `delete public IP and NIC when VM is deleted`. |
| Networking | Auto-shutdown | Click `enable auto-shutdown`. For *shutdown time*, type `11:59:00 PM`. For *time zone*, select `(UTC-05:00) Eastern Time (US & Canada)`. |
| Review + create | | When reviewing the VM, it should say `1 X Standard B1ms by Microsoft` and `0.0207 USD/hr`. |

#### 2. Install MySQL on VM 
- Connecting to the VM (Cloud Shell)
  1. In your terminal, type `ssh`.
  2. Type `ssh <username>@<ip address>`. Use the username and ip address from your VM on Azure.
  3. Type `sudo apt-get update` to update the UBUNTU OS.
- Installing and connecting to MySQL on the VM (Cloud Shell)
  1. Type `sudo apt install mysql-client mysql-server` to install MySQL.
  2. Type `sudo mysql`. This will connect you to the MySQL server as the root user.
  3. Type `CREATE USER `'<username>'@'%' IDENTIFIED BY '<password>';`. Create your own username and password. This will connect you to the MySQL server as a non-root user.
  4. Type 'GRANT ALL PRIVEGES ON *.* TO '<username>'@'%' WITH GRANT OPTION;`. This will grant privelegs to the non-root user.
- Allowing external connections (Cloud Shell)
  1. Do `control + D`.
  2. Type `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf` to change MySQL configurations.
  3. Set `bind-address = 0.0.0.0` and `mysqlx-bind-address = 0.0.0.0`.
  4. Do `control + O` to save.
  5. Press 'enter`.
  6. Do `control + X` to exit.
  7. Type `/etc/init.d/mysql restart`.
- Setting up a port (Azure)
  1. Go back to your VM on Azure.
  2. Click `network settings`.
  3. Scroll to inbound port rules and Click the drop down for `+create port rule`.
  4. Click `inbound port rule`.
  5. Service: `MySQL` (make sure destination port range is 3306).
  6. Click `add`.
     

  






