# insta_parser
Instagram photo parser

Main paths in graphql_json
1) graphql_json['entry_data']['ProfilePage'][0]['graphql']['user']
2) graphql_json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'] - the info of photos
3) for this path ['node']['display_url'] - specific photo


Main problem - download only first 12 photos
