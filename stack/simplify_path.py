def simplifyPath(path: str) -> str:
  # Split the path, with '/' as the delimiter.
  # For each token:
    # If '..', remove prior token
    # If '.' or '', continue
    # Otherwise, add to the stack

  tokens = []

  for token in path.split('/'):
    if token == '' or token == '.':
      continue
    
    if token == '..':
      if tokens:
        tokens.pop()

      continue

    tokens.append(token)

  
  # NOTE: Can be replaced with ' return '/' + '/'.join(stack) '
  new_fp = ''

  for token in tokens:
    new_fp += '/{tok}'.format(tok = token)

  return '/' if new_fp == '' else new_fp

print(simplifyPath("/home/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))