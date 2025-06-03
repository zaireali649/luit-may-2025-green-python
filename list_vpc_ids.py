import boto3  # AWS SDK for Python; allows you to interact with AWS services

vpc_client = boto3.client('ec2')  # Create a client for the EC2 service to interact with VPCs

response = vpc_client.describe_vpcs()  # Call the EC2 API to retrieve information about all VPCs

vpcs = response['Vpcs']  # Extract the list of VPCs from the response

for vpc in vpcs:  # Loop through each VPC in the list
    print(vpc['VpcId'])  # Print the unique ID of the VPC
