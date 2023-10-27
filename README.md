# DO NOT USE THIS REPO - MIGRATED TO GITLAB

# packer-egress-test
Lambda to test the internet egress endpoints required by Packer
 
[![Known Vulnerabilities](https://snyk.io//test/github/dwp/packer-egress-test/badge.svg?targetFile=requirements.txt)](https://snyk.io//test/github/dwp/packer-egress-test?targetFile=requirements.txt)

## Example Invocation
First create payload file:

`event.json`
```json
{
    "required_endpoints": {
      "GitHub":  "https://github.com",
      "DockerHub": "https://hub.docker.com"
    }
}
```

Then use AWS CLI to invoke the Lambda and await response

`aws lambda invoke --function-name packer_egress_test --invocation-type RequestResponse --payload file://event.json --cli-connect-timeout 600 --cli-read-timeout 600 output.json`