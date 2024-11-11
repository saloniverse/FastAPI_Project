from pydantic import BaseModel
from typing import Optional, Dict

class ServiceStatus(BaseModel):
	nfs: str
	ldap: str
	sshd: str

class InstalledStatus(BaseModel):
	splunk_agent: str
	mdatp_agent: str
	illumio_agent: str
	commvault_agent: str

class ServerRead(BaseModel):
	hostname: str
	server_class: str
	ip_address: str
	server_state: str
	patching_group: str
	business_owner: str
	os_version: str
	kernel_version: str
	service_status: ServiceStatus
	installed_agent: InstalledStatus