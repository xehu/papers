import re,itertools
with open('references.bib') as references:
  refs=references.read()

refObjects=re.findall("(@(?:.*?)\}\n\})\n", refs,re.MULTILINE|re.DOTALL)
print("Found {} references...".format(len(refObjects)))


# print(refObjects[0])
# quit()
bibliography=list()
longest_field=0

fieldName=re.compile("^\s*(\S+)\s*=\s*.*")

fields=list(map(lambda n:n.split("\n"),refObjects))
# print(refObjects[-1])
# quit()
# print(fields[0])

results=set()
for obj in fields:
  temp=set(itertools.chain(*filter(None,map(fieldName.findall,obj))))
  results=results.union(temp)
# print(results)
longest_field=max(results,key=lambda n:len(n))

# print(longest_field)
# quit()
for ref in refObjects:
# for line in refObjects[0].split("\n"):
  for line in ref.split("\n"):
    output=list()
    result=re.findall("^\s*(\S+)\s*=\s*\{(.*)\}(?:,|\})",line)
    # if result and result[0][0]=="year":
    #   print(result)
    #   quit()
    output.append("  {field}{space} = {{{entry}}},".format(field=result[0][0],
                                                           space=" "*(len(longest_field)+15-len(result[0][0])),
                                                           entry=result[0][1]) if result else line or "}")
    bibliography.append(output[0])
    print("\n".join(output))


# print("\n".join(bibliography))
for n in bibliography:
  print(n)