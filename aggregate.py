query_find = {
            'start_ts': {"$gte": start_date_str},
            'end_ts': {"$lte": end_date_str}
        }

query_group = {"_id": "$user_id"}

query_aggregate = [
    {
        "$match": query_find
    },
    {
        "$group": query_group
    }
]

cursor = self.user_grade_progress.aggregate(query_aggregate)
if cursor and cursor["ok"] == 1:
    # for item in cursor["result"]:
    return [item["_id"] for item in cursor["result"]]


#
#   Demo 2  projection
# 
start_date_str = start_date.isoformat() + "T00:00:00"
end_date_str = end_date.isoformat() + "T23:59:59"
query_find = {
    'user_id': user_id,
    'start_ts': {"$gte": start_date_str},
    'end_ts': {"$lte": end_date_str}
}
# query sample
# {'start_ts': {'$gte': '2016-07-01T00:00:00'}, 'end_ts': {'$lte': '2016-07-01T24:00:00'},
# 'user_id': '57574e4df92ea1255756cda9'}
projection = {
    "grade_id": 1,
    "user_id": 1,
    'end_ts': 1,
    "start_score": 1,
    "end_score": "$end_score_obj.projected_score"
}

query_group = {"_id": "$grade_id",
                "start_score": {"$first": "$start_score"},
                "end_score": {"$last": "$end_score"},
                }

# unfortunately score is string not float in database
# projection2 = {
#     "score_change": {"$subtract": ["end_score", "start_score"]}
# }
query_aggregate = [
    {
        "$match": query_find
    },
    {
        "$project": projection
    },
    {
        "$sort": {"end_ts": 1}
    },
    {
        "$group": query_group
    }
]

cursor = self.user_grade_progress.aggregate(query_aggregate)
if cursor and cursor["ok"] == 1:
    # for item in cursor["result"]:
    return [item for item in cursor["result"]]