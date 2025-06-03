from helpers import *  # Assumes helper functions like get_ec2_client and instance creation logic are imported

def create_instances(ec2_client: object, ami_type: str = "ubuntu", instance_amount: int = 1) -> None:
    """
    Creates EC2 instances based on the specified AMI type and instance count.

    Args:
        ec2_client (object): Boto3 EC2 client object used to interact with AWS EC2.
        ami_type (str, optional): Type of AMI to use for the instance. 
            Supported values are 'ubuntu', 'linux2023', and 'linux2'. Defaults to 'ubuntu'.
        instance_amount (int, optional): Number of instances to create. Defaults to 1.

    Returns:
        None
    """
    # Normalize the AMI type string: lowercase, remove leading/trailing spaces, and eliminate inner spaces
    cleaned_ami_type = ami_type.lower().strip().replace(" ", "")

    for i in range(instance_amount):
        if cleaned_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Create Ubuntu instance
            print("Created Ubuntu")
        elif cleaned_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)  # Create Amazon Linux 2023 instance
            print("Created Linux 2023")
        elif cleaned_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)  # Create Amazon Linux 2 instance
            print("Created Linux 2")
        else:
            print("Unsupported AMI Type")  # Handle unsupported AMI types

if __name__ == "__main__":
    ec2_client = get_ec2_client()  # Initialize the EC2 client

    # Create one Ubuntu instance (default)
    create_instances(ec2_client)

    # Create one Amazon Linux 2023 instance (extra spaces in type handled)
    create_instances(ec2_client, ami_type="linux  2023")

    # Create three Amazon Linux 2 instances
    create_instances(ec2_client, ami_type="linux 2", instance_amount=3)
