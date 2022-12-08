import sys

path_to_cwd = []
dirs = {}

for line in sys.stdin:
  line = line.strip()
  tokens = line.split(' ')

  # if this is a command
  if tokens[0] == '$':
    # we only care if this is a cd so we can track the path
    # to the cwd
    if tokens[1] == 'cd':
      cd_destination = tokens[2]

      if cd_destination == '/':
        path_to_cwd = ['']
      elif cd_destination == '..':
        path_to_cwd.pop()
      else:
        path_to_cwd.append(cd_destination)
  
  # this is not a command
  else:
    # if this is not a directory, it's a file
    # add its size to the total for the cwd and its parents
    if tokens[0] != 'dir':
      for i in range(len(path_to_cwd)):
        path = '/' + '/'.join(path_to_cwd[1:i+1])

        dirs.setdefault(path, 0)
        filesize = int(tokens[0])
        dirs[path] += filesize

TOTAL_DISK_SPACE = 70000000
REQUIRED_DISK_SPACE = 30000000

used_space = dirs['/']
free_space = TOTAL_DISK_SPACE - used_space
answer = TOTAL_DISK_SPACE

for space in dirs.values():
  free_if_deleted = free_space + space

  if free_if_deleted >= REQUIRED_DISK_SPACE and space < answer:
    answer = space

print(answer)
