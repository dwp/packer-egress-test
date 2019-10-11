# packer-egress-test
Lambda to test the internet egress endpoints required by Packer

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