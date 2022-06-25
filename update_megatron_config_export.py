import json 

with open('megatron_config_export.json') as json_file:
    data = json.load(json_file)

data['batch_size'] = 1        # originally 4
data['maximum_tokens'] = 40   # originally 10

with open('megatron_config_export.json', 'w') as outfile:
    json.dump(data, outfile)
