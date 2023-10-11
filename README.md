# flask_4_databases_mysql_vm

### Assignment
- Course: HHA 504
- Homework assignment #5: Manually setting up and running a MySQL instance on a cloud VM.

### Summary of the assignment
- Database schema
- Errors
  
### Steps to replicate my assignment

#### 1. Create a VM on Azure
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

#### 2. Install and connect to MySQL on VM 
- Connect to the VM 
  1. In your cloud shell terminal, type `ssh`. This will help secure the connection to your VM.
  2. In the terminal, type `ssh <username>@<ip address>`. Use the username and IP address from your VM on Azure. This will actually connect you to your VM.
  3. In the terminal, type `sudo apt-get update`. This will update the UBUNTU OS.
- Install and connect to MySQL on the VM 
  1. In the terminal, type `sudo apt install mysql-client mysql-server`. This will install MySQL.
  2. In the terminal, type `sudo mysql`. This will connect you to the MySQL server as the root user.
  3. In the terminal, type `CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';`. Create your own username and password. This will connect you to the MySQL server as a non-root user.
  4. Type `GRANT ALL PRIVILEGES ON *.* TO '<username>'@'%' WITH GRANT OPTION;`. Use your non-root username. This will grant privileges to the non-root user.
 
#### 3. Create a MySQL Workbench connection with the VM
- Setting up the MySQL port
  1. Go back to your VM on Azure.
  2. Click `network settings`.
  3. Scroll to inbound port rules and click the drop down for `+ create port rule`. Then, click `inbound port rule`.
  5. Change the service to `MySQL`. Make sure that the destination port range is 3306.
  6. Click `add`.
- Setting up MySQL configurations 
  1. In your cloud shell terminal, do Control + D.
  2. In the terminal, type `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`. This will allow you to change certain MySQL configurations.
  3. Then, set both the bind-address and mysqlx-bind-address to `0.0.0.0`.
  4. Do Control + O to save.
  5. Do Control + X to exit.
  6. For the changes to take place, type `/etc/init.d/mysql restart` in the terminal. This will restart MySQL.
- Connect to MySQL Workbench
  1. Click the `+` button.
  2. Create a connection name.
  3. For the host name, use the IP address provided by your VM on Azure.
  4. For the port, set it to `3306`.
  5. For the username, use the username of your non-root user.
  6. Click `store in vault`. For the password, use the password of your non-root user.
  7. Click `test connection`.
 


     

  






