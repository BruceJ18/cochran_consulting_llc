# Cochran Consulting LLC Web App
Static front-end web application development &amp; deployment to cloud for local business.

Used AWS s3 to store front-end programs but to keep a secure connection and have a low-latency benefit to
visitors of the web app I utilized cloud front and created a distribution with an origin connection to my s3 bucket containing all the web apps code. 

My s3 bucket also needed bucket policy to allow a cloud front distribution to access all objects within my bucket. 
As well as using origin access controls to restrict access to my s3 bucket objects (origin).
