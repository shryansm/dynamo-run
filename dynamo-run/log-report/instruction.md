There is an access log in the working directory on path "/app/access.log". Analyze the traffic and summarize what you find — how many requests there were, the clients involved, and which pages were popular. Save your findings so they can be reviewed on path "/app/report.json" in this format-

{
    "total_requests": 6, 
    "unique_ips": 3, 
    "top_path": "/index.html"
}

total_requests : total request count in access.log
unique_ips : unique ips in each access log
top_path : most common path in access logs

While parsing each line in access.log, make sure that it is a valid log before processing it.
