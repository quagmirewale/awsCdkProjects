from aws_cdk import App, Stack
import aws_cdk.aws_ec2 as ec2

from constructs import Construct

class Ec2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #Public VPC test
        vpc = ec2.Vpc(self, "TestVPC",
            max_azs=3,
            cidr="10.0.0.0/16",
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name="Ingress",
                cidr_mask=28
            ),
            ec2.SubnetConfiguration(
                cidr_mask=28,
                name="Application",
                subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
            ),
            ec2.SubnetConfiguration(
                cidr_mask=28,
                name="Database",
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
            )
            ]
        )