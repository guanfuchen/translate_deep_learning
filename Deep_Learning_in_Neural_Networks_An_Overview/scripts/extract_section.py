import re

tex_header = open('tex_header.tex').read()
tex_tail = open('tex_tail.tex').read()
tex = open('DeepLearning8Oct2014.tex').read()

#  abstract = re.findall(r'\\begin{abstract}(.*?)\\end{abstract}', tex, re.S)
#  print(abstract)

section = re.findall(r'\\section(.*?)%\\newpage', tex, re.S)
#  print(len(section))
#  print(section[0])
for section_index in len(section):
    if section_index > 0:
        section_tex = tex_header + tex + tex_tail

