from helpers import * 

def create_instances(ec2_client, ami_type="ubuntu", instance_amount=1):
    cleaned_ami_type = ami_type.lower().strip().replace(" ", "")

    for i in range(instance_amount):
        if cleaned_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif cleaned_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif cleaned_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("Unsupported AMI Type")

if __name__=="__main__":
    ec2_client = get_ec2_client()
    create_instances(ec2_client)
    create_instances(ec2_client, ami_type="linux  2023")
    create_instances(ec2_client, ami_type="linux 2", instance_amount=3)