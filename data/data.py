fake_db = [
	{	
		"hostname": "slc0001", 
		"server_class": "Linux Server",
		"ip_address": "192.168.1.10",
		"server_state": "Installed",
		"patching_group": "P1-Premium-2nd-Saturday",
		"business_owner": "saloni.saloni@wipro.com",
		"os_version": "RHEL 7.9",
		"kernel_version": "3.10.0-1160.118.1.el7.x86_64",
		"service_status": {
			"nfs": "active",
			"ldap": "inactive",
			"sshd": "active"
		},
		"installed_agent": {
			"splunk_agent": "yes",
            "mdatp_agent": "no",
			"illumio_agent": "yes",
			"commvault_agent": "yes"
		}
    },
    {
		"hostname": "slc0012", 
		"server_class": "Linux Server",
		"ip_address": "192.168.1.12",
		"server_state": "Retired",
		"patching_group": "P6-Premium-2nd-Saturday",
		"business_owner": "xyz@wipro.com",
		"os_version": "RHEL 9.4",
		"kernel_version": "5.14.0-427.42.1.el9_4.x86_64",
		"service_status": {
			"nfs": "active",
			"ldap": "active",
			"sshd": "active"
		},
		"installed_agent": {
			"splunk_agent": "yes",
			"mdatp_agent": "yes",
			"illumio_agent": "yes",
			"commvault_agent": "yes"
		}
    },
    {
		"hostname": "slc0023", 
		"server_class": "Linux Server",
		"ip_address": "192.168.1.13",
		"server_state": "Installed",
		"patching_group": "P12-Premium-2nd-Saturday",
		"business_owner": "abc@wipro.com",
		"os_version": "SUSE 15 SP5",
		"kernel_version": "5.3.18-150300.59.174.1-default",
		"service_status": {
			"nfs": "active",
			"ldap": "inactive",
			"sshd": "inactive"
		},
		"installed_agent": {
			"splunk_agent": "yes",
			"mdatp_agent": "no",
			"illumio_agent": "no",
			"commvault_agent": "yes"
		},
	},
    {
		"hostname": "defreon01", 
		"server_class": "Windows Server",
		"ip_address": "200.168.1.13",
		"server_state": "Installed",
		"patching_group": "P12-Premium-2nd-Saturday",
		"business_owner": "utkarsh@wipro.com",
		"os_version": "Windows",
		"kernel_version": "10.0",
		"service_status": {
			"nfs": "inactive",
			"ldap": "inactive",
			"sshd": "inactive"
		},
		"installed_agent": {
			"splunk_agent": "yes",
			"mdatp_agent": "no",
			"illumio_agent": "no",
			"commvault_agent": "no"
		}
    }
]