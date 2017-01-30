
import json
import collections

def tree():
	return collections.defaultdict(tree)

colours= tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000
colours['primary']['green'] = 0x00FF00
colours['primary']['blue'] = 0x0000FF
colours['secondary']['yellow'] = 0xFFFF00
colours['secondary']['aqua'] = 0x00FFFF
colours['secondary']['fuchsia'] = 0xFF00FF

print(json.dumps(colours, sort_keys=True, indent=4))


clone = colours

print(json.dumps(clone, sort_keys=True, indent=4))

given_key = 'primary'


def check_key(given_tree, give_key):
  for k in given_tree:
	if given_key in k:
		return True
		break
	print(k)
	while isinstance(k, dict):
		if given_key in k:
			return True
			break
  return False


if check_key(clone, given_key):
	print('{} IN the tree'.format(given_key) )
else:
	print('{} NOT IN the tree'.format(given_key) )

