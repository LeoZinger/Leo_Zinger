#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-98cfaa75', #ubuntu 14.04 AMI
    MinCount=1,
    MaxCount=1,
    KeyName="leo_aws_ec2_keypair",
    InstanceType='t2.micro')
print("Created a new AWS EC2 instance with Python, id = %s", instance[0].id)