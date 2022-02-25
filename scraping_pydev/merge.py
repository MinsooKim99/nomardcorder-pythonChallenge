def merge_list(*args): # 리스트들의 n번째요소끼리 2차원리스트로 합치는 함수
  length=len(args[0])
  result=[]
  for x in range(length):
    xth_mem=list()
    for arg in args:
      xth_mem.append(arg[x])
    result.append(xth_mem)
  return result