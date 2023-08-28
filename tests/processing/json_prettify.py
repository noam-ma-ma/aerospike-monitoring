import json

given_json_data= "{'/home/namespace.json/namespace view/namespace: test/24/migrations remaining/333/c/0': [{'metric': {}, 'value': [1692117541.477, '0']}], '/home/namespace.json/namespace view/namespace: test/24/migrations remaining/333/a/1': [{'metric': {}, 'value': [1692117541.495, '0']}], '/home/namespace.json/namespace view/namespace: test/24/% memory used/321/a/0': [{'metric': {}, 'value': [1692117541.504, '92']}], '/home/namespace.json/namespace view/namespace: test/24/% memory trend/49/a/0': [{'metric': {}, 'value': [1692117541.511, '92']}], '/home/namespace.json/namespace view/namespace: test/24/% memory trend/49/b/1': [{'metric': {}, 'value': [1692117541.516, '0']}], '/home/namespace.json/namespace view/namespace: test/24/namespace memory statistics/68/a/0': [{'metric': {}, 'value': [1692117541.521, '343597383.68']}], '/home/namespace.json/namespace view/namespace: test/24/namespace memory statistics/68/b/1': [{'metric': {}, 'value': [1692117541.527, '4294967296']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/c/0': [{'metric': {}, 'value': [1692117541.534, '0']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/d/1': [{'metric': {}, 'value': [1692117541.544, '0']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/b/2': [{'metric': {}, 'value': [1692117541.549, '0']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/a/3': [{'metric': {}, 'value': [1692117541.554, '7498255']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/e/4': [{'metric': {}, 'value': [1692117541.559, '0']}], '/home/namespace.json/namespace view/namespace: test/24/objects/100/f/5': [{'metric': {}, 'value': [1692117541.565, '0']}], '/home/namespace.json/namespace view/namespace: test/24/% storage used/31/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/% storage used/31/b/1': [], '/home/namespace.json/namespace view/namespace: test/24/% device trend/27/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/% device trend/27/d/1': [], '/home/namespace.json/namespace view/namespace: test/24/% device trend/27/b/2': [{'metric': {}, 'value': [1692117541.592, '0']}], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/b/1': [], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/c/2': [], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/d/3': [], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/e/4': [], '/home/namespace.json/namespace view/namespace: test/24/namespace storage statistics/288/f/5': [], '/home/namespace.json/namespace view/namespace: test/24/partitions/358/a/0': [{'metric': {}, 'value': [1692117541.638, '0']}], '/home/namespace.json/namespace view/namespace: test/24/partitions/358/b/1': [{'metric': {}, 'value': [1692117541.642, '0']}], '/home/namespace.json/namespace view/namespace: test/24/sindexes/373/c/0': [{'metric': {}, 'value': [1692117541.647, '1']}], '/home/namespace.json/namespace view/namespace: test/24/set index populating/375/c/0': [{'metric': {'cluster_name': '63flash', 'ns': 'test'}, 'value': [1692117541.652, '0']}], '/home/namespace.json/namespace view/namespace: test/24/stop writes / hwm breached/113/a/0': [{'metric': {}, 'value': [1692117541.657, '1']}], '/home/namespace.json/namespace view/namespace: test/24/stop writes / hwm breached/113/b/1': [{'metric': {}, 'value': [1692117541.662, '0']}], '/home/namespace.json/namespace view/namespace: test/24/stop writes / hwm breached/113/c/2': [{'metric': {}, 'value': [1692117541.666, '0']}], '/home/namespace.json/namespace view/namespace: test/24/% primary index device used (flash/pmem)/305/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/% primary index device used (flash/pmem)/305/b/1': [], '/home/namespace.json/namespace view/namespace: test/24/namespace index (flash/pmem) usage/345/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/namespace index (flash/pmem) usage/345/b/1': [], '/home/namespace.json/namespace view/namespace: test/24/namespace index (flash/pmem) allocated/361/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/namespace index (flash/pmem) allocated/361/b/1': [], '/home/namespace.json/namespace view/namespace: test/24/nsup metrics/722/b/0': [{'metric': {}, 'value': [1692117541.701, '3']}], '/home/namespace.json/namespace view/namespace: test/24/nsup metrics/722/d/1': [{'metric': {}, 'value': [1692117541.706, '3']}], '/home/namespace.json/namespace view/namespace: test/24/nsup metrics/722/a/2': [{'metric': {}, 'value': [1692117541.71, '0']}], '/home/namespace.json/namespace view/namespace: test/24/nsup metrics/722/c/3': [{'metric': {}, 'value': [1692117541.715, '0']}], '/home/namespace.json/namespace view/namespace: test/24/% set quota used/741/a/0': [], '/home/namespace.json/namespace view/namespace: test/24/defrag sleep/975/d/0': [], '/home/namespace.json/namespace view/namespace: test/24/defrag low water mark/977/e/0': [], '/home/namespace.json/namespace view/namespace: test/24/defrag reads & writes /859/defrag_reads/0': [], '/home/namespace.json/namespace view/namespace: test/24/defrag reads & writes /859/defrag_writes/1': [], '/home/namespace.json/namespace view/namespace: test/24/defrag q/1105/a/0': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client reads (tps)/177/b/0': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client reads (tps)/177/a/1': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client reads (tps)/177/c/2': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client reads (tps)/177/d/3': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client reads (tps)/177/e/4': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client writes (tps)/179/b/0': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client writes (tps)/179/a/1': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client writes (tps)/179/c/2': [], '/home/namespace.json/namespace view/throughput (read, write)/181/client writes (tps)/179/d/3': []}"

json_object = json.loads( given_json_data)
json_formatted_str = json.dumps(json_object, indent=2)

print( json_formatted_str)
