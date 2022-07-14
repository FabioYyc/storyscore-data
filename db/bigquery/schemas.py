from google.cloud import bigquery
user_schema = [
        bigquery.SchemaField("name", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("email", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("username", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("type", bigquery.enums.SqlTypeNames.STRING),
    ]
commit_schema = [
        bigquery.SchemaField("sha", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("message", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("username", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("commit_date", bigquery.enums.SqlTypeNames.DATETIME),
    ]

pull_request_review_schema = [
        bigquery.SchemaField("body", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("state", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("pull_number", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("username", bigquery.enums.SqlTypeNames.STRING),
    ]
pull_request_schema = [
        bigquery.SchemaField("assignee_username", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("email", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("pull_number", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("state", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("reviews", "RECORD", mode="REPEATED", fields = pull_request_review_schema)
    ]
activity_schema = [*user_schema, 
 bigquery.SchemaField("commits", "RECORD", mode="REPEATED", fields = commit_schema),
 bigquery.SchemaField("pull_requests", "RECORD", mode="REPEATED", fields = pull_request_schema),
 bigquery.SchemaField("pull_request_reviews", "RECORD", mode="REPEATED", fields = pull_request_review_schema)
]