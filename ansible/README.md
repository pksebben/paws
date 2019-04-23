# Getting started

## Install Ansible

Follow the installation guide provided by ansible. Install ansible into a virtualenv (using virtualenvwrapper, preferably). Use the provided requirements.txt to get this all done quickly:

```
pip install -r requirements.txt
```

## Environment variables/Shell setup

Assuming you have already setup the path to your google service account json credentials, add the following to your profile:

```
export GCP_AUTH_KIND="serviceaccount"
export GCP_SERVICE_ACCOUNT_EMAIL="ian@pawsyourgame.org"
export GCP_SERVICE_ACCOUNT_FILE=$GOOGLE_CLOUD_KEYFILE_JSON
cp $GOOGLE_CLOUD_KEYFILE_JSON /tmp/serviceaccount.json
export ANSIBLE_REMOTE_USER=$(echo $GCP_SERVICE_ACCOUNT_EMAIL | tr "@." _)
```

Obviously, change the email to match your IAM email address associated with PYG.

## Give it all a quick test

```
ansible web -m ping
```
