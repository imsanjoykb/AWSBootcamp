# HammerDB Instance

Deploy HammerDB on AWS EC2 Linux and a Test Database. This is for reference only. 
Consider removing database secrets from templates.

This repo also contains a template to deploy dms to perform cdc from RDS to S3. 

For reference on the HammerDB TPC test see https://www.hammerdb.com/docs/ch03s05.html

### 1. Deploy HammerDB template with AWS CLI
```
    aws cloudformation create-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --parameters ParameterKey=DBInstanceClass,ParameterValue=db.m5.large \
    ParameterKey=DBIops,ParameterValue=3000 \
    --capabilities CAPABILITY_IAM
````

### 2. Running hammerdb and initialize the tpcc schema

1. CD into HammerDB home directory
2. Run ``./hammerdbcli``
3. Run ``librarycheck``
4. Run ``dbset db pg``
5. Run ``buildschema``. Wait until you see message "ALL VIRTUAL USERS COMPLETE" (~2 min)
6. Exit the hammerdb cli by typing  ``exit``

