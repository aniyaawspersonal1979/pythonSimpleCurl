# MacAddress Vendor details

This script helps you to know the vendor details of the macaddress what you pass

### Execution

Make sure that you have installed docker inorder to run the below code

```sh
$ git clone https://github.com/shan5a6/pythonSimpleCurl.git
$ cd pythonSimpleCurl
$ docker build -t "yourimage" .
```

### Testing
```sh
$ docker run yourimage:v1 python /opt/mac_address_check.py

output:
Please pass mac address for reference check below example
********Example*********
docker run mycustomimage:v1 python /opt/mac_address_check.py 44:38:39:ff:ef:57

```

### Sample Example

```sh
$ docker run yourimage:v1 python /opt/mac_address_check.py 44:38:39:ff:ef:57

output:
Vendor name is "Cumulus Networks, Inc"
```

