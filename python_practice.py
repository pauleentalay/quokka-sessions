import boto3

mgn = boto3.client('mgn')

response = mgn.describe_source_servers()

source_server_items = response['items']
# print(f"length of items: {len(items)}")
# print(type(items))

print("THE Source server IDs")
source_server_ids = []

for source_server in source_server_items:
    source_server_ids.append(source_server['sourceServerID'])

print(source_server_ids)


# list comprehension
fancy_ss_ids = [source_server['sourceServerID'] for source_server in response['items']]
print(f'type: {type(fancy_ss_ids)}, contents: {fancy_ss_ids}')


# for item in items:
#     print('######')
#     print(item)
#     print(type(item))

#print(response)


# students = ['cat', 'dog', 'frog', 'cat', [1,2,3], {'egg':'breakfast', 'milk': 'breakfast'}]
# my_pet = students[1]
# my_dictionary = students[5]
# print(my_dictionary)


# my_meals = {'egg':'breakfast', 'milk': 'breakfast', 'rice': ['lunch', 'dinner']}
# my_rice = my_meals['rice'][1]
# print(my_rice)


# def lambda_handler(event, context):
#     #print("Received event: " + json.dumps(event, indent=2))

#     # Get the object from the event and show its content type
#     bucket = event['Records'][0]['s3']['bucket']['name']
#     key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
#     try:
#         response = s3.get_object(Bucket=bucket, Key=key)
#         print("CONTENT TYPE: " + response['ContentType'])
    