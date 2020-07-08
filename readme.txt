Simple flask app that can be deployed to Google Cloud Run or GKE. 

All endpoints work when deployed on Cloud Run.

When Deployed on GKE, the "firepost" endpoint fails due to an unauthorized database request.

Use Cloud Build to upload and build the container image
gcloud builds submit
