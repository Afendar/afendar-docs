# Enable or disable maintenance mode

*Last update: September 24, 2024*

**Topics**: Install

**CREATED FOR**: Experienced | Admin | Developer

The following guide refers to a standard maintenance mode page. If you need to use a custom maintenance page, see Create the custom maintenance page topic.

Adobe Commerce uses maintenance mode to disable bootstrapping. Disabling bootstrapping is helpful while you are maintaining, upgrading, or reconfiguring your site.

The application detects maintenance mode as follows:

If var/.maintenance exists, maintenance mode is on, and the application will return a 503 maintenance page.
If var/.maintenance.ip exists, and the client IP corresponds to one of the IP address entries within this file, the maintenance page is ignored for the request.
Install the application
Before you use this command to enable or disable maintenance mode, you must install the application.

Enable or disable maintenance mode
Use the magento maintenance CLI command to enable or disable maintenance mode.

Command usage:

```cmd
bin/console maintenance:enable [--ip=<ip address> ... --ip=<ip address>] | [ip=none]
```
```cmd
bin/console maintenance:disable [--ip=<ip address> ... --ip=<ip address>] | [ip=none]
```
```cmd
bin/console maintenance:allow-ips <ip address> .. <ip address> [--none]
```
```cmd
bin/console maintenance:status
```

The --ip=<ip address> option is an IP address to exempt from maintenance mode (for example, developers doing the maintenance). To exempt more than one IP address in the same command, use the option multiple times.

NOTE
Using --ip=<ip address> with magento maintenance:disable saves the list of IPs for later use. To clear the list of exempt IPs, use magento maintenance:enable --ip=none or see Maintain the list of exempt IP addresses.
The bin/console maintenance:status command displays the status of maintenance mode.

For example, to enable maintenance mode with no IP address exemptions:

```cmd
bin/console maintenance:enable
```

To enable maintenance mode for all clients except 192.0.2.10 and 192.0.2.11:

```cmd
bin/console maintenance:enable --ip=192.0.2.10 --ip=192.0.2.11
```

After you place the application in maintenance mode, you must stop all message queue consumer processes.
One way to find these processes is to run the ps -ef | grep queue:consumers:start command, and then run the kill <process_id> command for each consumer. In a multiple node environment, repeat this task on each node.

Maintain the list of exempt IP addresses
To maintain the list of exempt IP addresses, you can either use the [--ip=<ip list>] option in the preceding commands or you can use the following:

```cmd
bin/console maintenance:allow-ips <ip address> .. <ip address> [--none]
```
The <ip address> .. <ip address> syntax is an optional space-delimited list of IP addresses to exempt.

The --none option clears the list.