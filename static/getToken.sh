#!/bin/bash
curl https://api.att.com/oauth/token --request POST --insecure --data "client_id=$1&client_secret=$2&grant_type=client_credentials&scope=SPEECH"

#curl "https://api.att.com/oauth/token" \
#    --header "Content-Type: application/x-www-form-urlencoded" \
#    --header "Accept: application/json" \
#    --data "client_id=$1&client_secret=$2&scope=SPEECH&grant_type=client_credentials" \
#    --request POST
