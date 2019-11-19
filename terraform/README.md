# Terraform for Paws Your Game

All terraform and terraform state should be checked in here. The state
must always match the configuration on merge.

## Getting Started

1. Install Terraform

2. Get your service account json file, download somewhere.

3. Add the following to your profile:
   ```export GOOGLE_CLOUD_KEYFILE_JSON="/Users/ianschenck/Downloads/Paws Your Game Main-8e7d17e9fbc5.json"```

4. Run `terraform init` to get initialize all plugins/resources.

## Change Workflow

1. Make changes where necessary, do NOT apply. Only plan.

2. Submit a diff/pull request, add the plan output to the pull request description.

3. Once approved, apply, _commit again to record the state_, and merge.

