import boto3
iamResoruce = boto3.resource('iam')
def lambda_handler(event, context):
    ACCOUNT_ID = context.invoked_function_arn.split(":")[4]
    Policies=iamResoruce.policies.all()
    for policy in Policies:
        if ACCOUNT_ID in policy.arn:
            policyObj = iamResoruce.Policy(policy.arn)
            PolicyVersion = iamResoruce.PolicyVersion(policyObj.arn,policyObj.default_version.version_id)
            if(isinstance(PolicyVersion.document['Statement'],list)):
                if(isinstance(PolicyVersion.document['Statement'][0]['Action'],list)):
                    for action in PolicyVersion.document['Statement'][0]['Action']:
                        print(" Policy Name:", policy.arn, "IAM Action:", action)
                else:
                    action = PolicyVersion.document['Statement'][0]['Action']
                    print(" Policy Name:", policy.arn, "IAM Action:", action )
            else:
                action = PolicyVersion.document['Statement']['Action']
                print(" Policy Name:", policy.arn, "IAM Action: ", action)
                        
